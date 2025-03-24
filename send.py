import requests

URL = "https://api.challenge.hennge.com/challenges/003"

body = {
  "github_url": "https://gist.github.com/MichaelPells/dc6a80a309a866999c259645cfec65ce",
  "contact_email": "themichaelpells@gmail.com",
  "solution_language": "python"
}

requests.post(URL,
              json = body
              )