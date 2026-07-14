import requests

def check_zoe_solar_keys():
    print("========================================")
    print("    ZOE Solar OCR - API Key Validator   ")
    print("========================================\n")

    # 1. NVIDIA API (Primary OCR)
    print("--- 1. NVIDIA API (NIM) ---")
    nv_key = "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"
    nv_url = "https://integrate.api.nvidia.com/v1/models"
    try:
        res = requests.get(nv_url, headers={"Authorization": f"Bearer {nv_key}"})
        if res.status_code == 200:
            print("✅ Status: ACTIVE (NVIDIA key is recognized)")
        elif res.status_code == 401:
            print("❌ Status: INVALID OR REVOKED")
        else:
            print(f"⚠️ Unexpected response: {res.status_code}")
    except Exception as e:
        print(f"❌ Network error: {e}")

    # 2. Google Gemini API
    print("\n--- 2. Google Gemini API ---")
    gem_key = "AIzaSyBaH6sO1vVs14N1tZinSBG3QFtynF6OUWk"
    gem_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={gem_key}"
    try:
        res = requests.get(gem_url)
        if res.status_code == 200:
            print("✅ Status: ACTIVE (Gemini key is recognized)")
        elif res.status_code == 400 and "API_KEY_INVALID" in res.text:
            print("❌ Status: INVALID OR REVOKED")
        else:
            print(f"⚠️ Response {res.status_code}: Make sure the key isn't restricted.")
    except Exception as e:
        print(f"❌ Network error: {e}")

    # 3. SiliconFlow API
    print("\n--- 3. SiliconFlow API ---")
    sf_key = "sk-iawnupcgvjfhbcgmyjdgarnuznulqtvphzyspsrwsfyspply"
    sf_url = "https://api.siliconflow.cn/v1/user/info"
    try:
        res = requests.get(sf_url, headers={"Authorization": f"Bearer {sf_key}"})
        if res.status_code == 200:
            print("✅ Status: ACTIVE (SiliconFlow key is recognized)")
        elif res.status_code == 401:
            print("❌ Status: INVALID OR REVOKED")
        else:
            print(f"⚠️ Unexpected response: {res.status_code}")
    except Exception as e:
        print(f"❌ Network error: {e}")

    # 4. Supabase (Custom Domain)
    print("\n--- 4. Supabase Anon Key ---")
    sb_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIn0.oqN5J2n6GBoLIf3OpsUrK2OZWIAINIWcbmRV0mtA4yQ"
    sb_url = "https://supabase.aura-call.de/auth/v1/settings"
    try:
        # Supabase requires both the apikey and Authorization header
        res = requests.get(sb_url, headers={
            "apikey": sb_key,
            "Authorization": f"Bearer {sb_key}"
        })
        if res.status_code == 200:
            print("✅ Status: ACTIVE (Supabase URL and Anon key are functioning)")
        elif res.status_code == 401:
            print("❌ Status: INVALID OR REVOKED (JWT signature failed)")
        elif res.status_code == 404:
            print("❌ Status: NOT FOUND (Check if supabase.aura-call.de is online)")
        else:
            print(f"⚠️ Unexpected response: {res.status_code}")
    except Exception as e:
        print(f"❌ Network error: {e}")

    # 5. GitLab Personal Access Token
    print("\n--- 5. GitLab Cloud Storage Token ---")
    gl_token = "glpat-UlPiC_d-Ede-SBr46lgeDW86MQp1Omo5a2RwCw.01.120885tzr"
    gl_url = "https://gitlab.com/api/v4/user"
    try:
        res = requests.get(gl_url, headers={"PRIVATE-TOKEN": gl_token})
        if res.status_code == 200:
            user = res.json().get('username', 'Unknown User')
            print(f"✅ Status: ACTIVE (Token provides access to GitLab user: {user})")
        elif res.status_code == 401:
            print("❌ Status: INVALID OR REVOKED")
        else:
            print(f"⚠️ Unexpected response: {res.status_code}")
    except Exception as e:
        print(f"❌ Network error: {e}")

if __name__ == "__main__":
    check_zoe_solar_keys()