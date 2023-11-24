def determine_background_color(weather_data: dict) -> str:
    main_weather = weather_data["weather"][0]["main"].lower()
    if main_weather in ["snow", "rain"]:
        return "blue"
    elif main_weather in ["clear"]:
        return "red"
    elif main_weather in ["clouds"]:
        return "orange"
    else:
        return "gray"  # default color
