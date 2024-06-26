import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Cấu hình ứng dụng Lark
APP_ID = os.getenv("LARK_APP_ID")
APP_SECRET = os.getenv("LARK_APP_SECRET")
REDIRECT_URI = os.getenv("LARK_REDIRECT_URI")

def get_login_url():
    return f"https://open.larksuite.com/open-apis/authen/v1/authorize?app_id={APP_ID}&redirect_uri={REDIRECT_URI}&response_type=code"

def exchange_code_for_token(code):
    url = "https://open.larksuite.com/open-apis/authen/v1/access_token"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error exchanging code for token: {str(e)}")
        if response is not None:
            st.error(f"Response content: {response.text}")
        return None

def main():
    st.title("Lark Login Example")
    
    # Hiển thị video demo
    st.video("20240627001122_rec_.mp4")
    
    # Xử lý đăng xuất
    if st.session_state.get('logout'):
        st.session_state.clear()
        st.rerun()

    if "user_info" not in st.session_state:
        if "code" in st.query_params:
            code = st.query_params.get("code")
            token_response = exchange_code_for_token(code)
            if token_response and token_response.get('code') == 0:
                user_data = token_response.get('data', {})
                st.session_state.user_info = {
                    'name': user_data.get('name'),
                    'en_name': user_data.get('en_name'),
                    'avatar_url': user_data.get('avatar_url'),
                    'email': user_data.get('email'),
                    'enterprise_email': user_data.get('enterprise_email'),
                    'mobile': user_data.get('mobile'),
                    'open_id': user_data.get('open_id'),
                    'user_id': user_data.get('user_id'),
                    'access_token': user_data.get('access_token')
                }
            else:
                st.error("Failed to get user information")
                if token_response:
                    st.error(f"Error details: {token_response}")
            # Xóa code từ query params sau khi sử dụng
            st.query_params.clear()
            st.rerun()
        else:
            login_url = get_login_url()
            st.write(f"[Login with Lark]({login_url})")

    if "user_info" in st.session_state:
        st.write("User Information:")
        st.write(f"Name: {st.session_state.user_info['name']}")
        st.write(f"English Name: {st.session_state.user_info['en_name']}")
        st.image(st.session_state.user_info['avatar_url'], width=100)
        st.write(f"Email: {st.session_state.user_info['email']}")
        st.write(f"Enterprise Email: {st.session_state.user_info['enterprise_email']}")
        st.write(f"Mobile: {st.session_state.user_info['mobile']}")
        st.write(f"Open ID: {st.session_state.user_info['open_id']}")
        st.write(f"User ID: {st.session_state.user_info['user_id']}")
        
        if st.button("Logout"):
            st.session_state['logout'] = True
            st.rerun()

if __name__ == "__main__":
    main()