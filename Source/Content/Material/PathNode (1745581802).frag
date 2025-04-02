// Shader "Default/Renderer/Fragment.glsl"
#include "Default/Header.glsl"

// Inputs from the Vertex Shaders:
in VS_OUT{
	vec3 normal;
	vec3 tangent;
	vec2 texCoord;
	vec3 position;
} fsIn;
in vec4       entityTint;
flat in ivec4 entityID;

// Fragment Shader Outputs:
layout(location = 0) out vec4 gColor;
layout(location = 1) out vec4 gNormal;
layout(location = 2) out vec4 gAssetID;

#include "Default/Uniforms/Scene.glsl"  // inScene
#include "Default/Uniforms/Lights.glsl" // inLights
#include "Default/Uniforms/Material.glsl"

#include "Math/Random.glsl"
#include "Math/Pbr.glsl"

#ifndef SHADER_SHADOW_PASS // Regular pass bellow:

void mainBasic() { // You can use this one to test things out... :)
	gAssetID = entityID;

	vec2 uv = m_GetUV();
	gNormal = vec4(m_GetNormal(uv), GetDistanceToCamera());
	gColor = texture(m_albedo, uv);
}

void main() {
	gAssetID = entityID;

	vec3 uvs = m_GetUVS(1); // UV + Displacement Shadows
	vec2 uv = uvs.xy;

	gNormal = vec4(m_GetNormal(uv), GetDistanceToCamera());

	vec4 albedo = texture(m_albedo, uv);
	albedo.rgb *= entityTint.rgb;

	// LOD Dithering if the tint alpha is negative:
	if (entityTint.a < 0) {
		if (abs(entityTint.a) < Random(fsIn.position)) {
			discard;
		}
	}
	else {
		albedo.a *= entityTint.a;
	}
	albedo.a *= m_alphaFactor;

	#ifndef SHADER_ALPHA_BLEND
		float alphaThreshold = m_alphaFactor - 0.01f; // - Bias
		if (albedo.a < alphaThreshold || albedo.a <= 0.f) {
			discard;
		}
	#endif

	#ifdef SHADER_MATERIAL_SHADELESS
		gColor = albedo;
	#else // Not Shadeless:
		gColor = vec4(0,0,0,1);

		float shadow = 1.0;
		#ifdef SHADER_SCENE_HAS_SHADOWS
			// Normal here is only used for extra Bias,so we use the model one!
			shadow = GetSceneShadow(fsIn.normal, fsIn.position);
			shadow = mix(0.0, mix(1.0, uvs.z, inScene.shadowInfluence), shadow);

			// FYI: You can also use GetSceneShadowDebug (returns a vec3 with 
			// float shadow + vec2 cascade number) for DEBUGGING PURPOSES!
		#endif

		float metallic = texture(m_metallicFactor, uv).x;
		float roughness = texture(m_roughnessFactor, uv).x;

		#ifdef SHADER_SCENE_HAS_AMBIENT
			gColor.xyz = GetSceneAmbientFor(uv, albedo.xyz, gNormal.xyz, fsIn.position, metallic, roughness);
		#endif 

		#ifdef SHADER_SCENE_SHADED
			gColor.xyz += GetPbrColor(gNormal.xyz, shadow, albedo.xyz, metallic, m_isMetal, roughness);
		#endif
	#endif

	gColor.xyz += texture(m_emission, uv).rgb * m_emissionScale;

	#ifdef SHADER_SCENE_HAS_MIST
		gColor.xyz = GetSceneMistFor(gColor.xyz, gNormal.xyz, fsIn.position);
	#endif

	#ifdef SHADER_ALPHA_BLEND
		gColor.a = albedo.a;
	#endif
}

#else // SHADER_SHADOW_PASS || Shadow pass bellow:

void main() {
	// LOD Dithering if the tint alpha is negative:
	if (entityTint.a < 0) {
		if (abs(entityTint.a) < fract(length(fsIn.position))) {
			discard;
		}
	}

	// The shadow pass only updates the albedo texture is alphaValue is < 1.0!
	if (m_alphaFactor < 0.99999f) {
		vec2 uv = m_GetUV();
		vec4 albedo = texture(m_albedo, uv);
				
		// Only multiply the tint if entityTint.a >= 0:
		albedo.a *= mix(1.0, entityTint.a, float(entityTint.a >= 0));
		albedo.a *= m_alphaFactor;

		float alphaThreshold = m_alphaFactor - 0.01f; // - Bias
		if (albedo.a < alphaThreshold) {
			discard; // Discard alpha
		}
	}
}

#endif // SHADER_SHADOW_PASS