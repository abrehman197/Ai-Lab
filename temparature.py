import streamlit as st

# Function to convert the temperature
def convert_temperature(value, from_unit, to_unit):
    # Celsius to Fahrenheit, Kelvin, etc.
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        elif to_unit == "Celsius":
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif to_unit == "Fahrenheit":
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        elif to_unit == "Kelvin":
            return value

# Streamlit UI
st.title("🌡️ Temperature Converter")

# Input for temperature value
temperature = st.number_input("Enter Temperature", min_value=-273.15, format="%.2f")

# Dropdowns for selecting the units
temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
from_unit = st.selectbox("From Unit", temperature_units)
to_unit = st.selectbox("To Unit", temperature_units)

# Button to perform the conversion
if st.button("Convert"):
    if from_unit == to_unit:
        st.error("Please choose different units to convert.")
    else:
        # Perform the conversion
        converted_value = convert_temperature(temperature, from_unit, to_unit)
        st.success(f"{temperature} {from_unit} is equal to {converted_value:.2f} {to_unit}")
