import requests


def get_weather() -> None:
    api_key = "3213a637c33d45b4a5794241252305"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Lviv&lang=uk"
    response = requests.get(url)
    data = response.json()

    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Погода у Львові: {temperature}°C, {condition}")


if __name__ == "__main__":
    get_weather()
