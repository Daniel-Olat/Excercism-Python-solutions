// Package weather forecasts the current weather conditons of variuos cities.
package weather


var (
    // CurrentCondition gives the current condition of any city on goblinocus.
	CurrentCondition string
    // CurrentLocation gives the location of the city whose weather is being determined.
	CurrentLocation  string
)
// Forecast gives the full weather forcast of a particular city forecast of a particular city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
