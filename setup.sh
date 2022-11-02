mkdir -p ~/.streamlit/
echo "\
[general]\n\
email =\"vicente35713@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml