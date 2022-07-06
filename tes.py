import urllib.request

url = "https://instagram.fcgk37-1.fna.fbcdn.net/v/t51.2885-19/271800728_4545632342201375_4535251099111566974_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fcgk37-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=hQvC58e-8nwAX_fyrVh&edm=AABBvjUBAAAA&ccb=7-5&oh=00_AT_lkl4KupnVyu2WTOHVpRBCMI9Kt6b0MkGCJtkUHJUWFQ&oe=62CB8F7B&_nc_sid=83d603"

r = urllib.request.urlopen(url)
with open("wind_turbine.jpg", "wb") as f:
    f.write(r.read())