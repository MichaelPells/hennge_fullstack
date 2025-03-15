import requests

url = "https://api.challenge.hennge.com/challenges/003"

body = {
  "github_url": "https://gist.github.com/MichaelPells/GIST_ID",
  "contact_email": "themichaelpells@gmail.com",
  "solution_language": "python"
}

# requests.post()