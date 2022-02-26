# Deploying to Heroku

### Heroku Setup
```sh
# st_setup.sh
mkdir -p ~/.streamlit
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

```Procfile
web: sh st_setup.sh && streamlit run app.py
```

### Deployment
```sh
heroku create northdash
heroku git:remote -a northdash
git push heroku main
```

### Additional Resources
1. 
https://towardsdatascience.com/deploying-a-basic-streamlit-app-to-heroku-be25a527fcb3

