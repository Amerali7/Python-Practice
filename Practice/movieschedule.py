movies = {
'The g':'11:00am',
'Rudolph':'1:00pm',
'frosty':'3:00'
}
print("We r showing the following movies")

for key in movies:
    print(key)

movieshow = input('what movie would you like the showtime for?\n')


showtime = movies.get(movieshow)
if showtime ==None:
    print("movie not showing")
else:
    print(movieshow,'is playing at', showtime)