import requests

url = "https://ambee-soil-data.p.rapidapi.com/soil/history/by-lat-lng"

querystring = {"lat":"20.59","lng":"78.96","startDate":"'YYYY-MM-DD hh:mm:ss'","endDate":"YYYY-MM-DD hh:mm:ss''"}

headers = {
	"X-RapidAPI-Key": "30421f4308msh9ce9bfb33f057bfp1dfbd1jsnb97d41a029c0",
	"X-RapidAPI-Host": "ambee-soil-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)