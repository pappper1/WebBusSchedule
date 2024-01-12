import requests


cookies = {
    'ASP.NET_SessionId': 'oclmsz4t3r1o5h1i3hvtwmxa',
    '__RequestVerificationToken_L2xvb2tvdXRfeWFyZA2': 'DrNenWqq6Gmijfg3VvzI3RMVmhyLcl2hbqyYrTl9e2YeK0eZghc5ufeknk0iXbKtg2IrAsAWFTHUBf86Kta3BMdRDr40hHZufgNkSVV4DTE1',
    '_ga': 'GA1.1.950650976.1700487850',
    '_ga_CZQSPX20W4': 'GS1.1.1701013858.2.1.1701014567.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'ASP.NET_SessionId=oclmsz4t3r1o5h1i3hvtwmxa; __RequestVerificationToken_L2xvb2tvdXRfeWFyZA2=DrNenWqq6Gmijfg3VvzI3RMVmhyLcl2hbqyYrTl9e2YeK0eZghc5ufeknk0iXbKtg2IrAsAWFTHUBf86Kta3BMdRDr40hHZufgNkSVV4DTE1; _ga=GA1.1.950650976.1700487850; _ga_CZQSPX20W4=GS1.1.1701013858.2.1.1701014567.0.0.0',
    'Origin': 'https://www.minsktrans.by',
    'Referer': 'https://www.minsktrans.by/lookout_yard/Home/Index/minsk',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

class Parser:
    def __init__(self):
        self.headers = headers
        self.cookies = cookies
    def route_list(self):
        data = {
            'p':'minsk',
            'tt':'bus',
            '__RequestVerificationToken':'21SCGAuckxj5t_h7WUb-teynN9DNHD9ETFpFahbd8P7oKeEIVgLI8yHE3eQItubIdTOotjKvhWg2JaRNLNkeVuXO7Ms8t732MulY8qo_avs1',
        }

        response = requests.post('https://www.minsktrans.by/lookout_yard/Data/RouteList', cookies=self.cookies,
                                headers=self.headers, data=data).json()

        routes = [route['Number'] for route in response['Routes']]

        return tuple(routes)


    def route_info(self, bus_route):
        data = {
            'p':'minsk',
            'tt':'bus',
            'r':bus_route,
            '__RequestVerificationToken':'Vq5bY__Kz-cNY5gGFK6nH1HrxinKivqgwzCJC84PbYcNp-Qr9Hs4S7aX7RYjIyII33V_j7_Eb4ZD02PxQuHfiKi9hGg23HUGCujU2w9Z8P01',
        }

        response = requests.post('https://www.minsktrans.by/lookout_yard/Data/Route', cookies=self.cookies, headers=self.headers,
                                 data=data).json()

        route_a = response['Trips']['NameA']
        route_b = response['Trips']['NameB']

        return route_a, route_b

    def stops(self, bus_route):
        data = {
            'p':'minsk',
            'tt':'bus',
            'r':bus_route,
            '__RequestVerificationToken':'Vq5bY__Kz-cNY5gGFK6nH1HrxinKivqgwzCJC84PbYcNp-Qr9Hs4S7aX7RYjIyII33V_j7_Eb4ZD02PxQuHfiKi9hGg23HUGCujU2w9Z8P01',
        }

        response = requests.post('https://www.minsktrans.by/lookout_yard/Data/Route', cookies=self.cookies, headers=self.headers,
                                 data=data).json()
        route_a = response['Trips']['NameA']
        route_b = response['Trips']['NameB']

        directions = {
            0: route_a,
            1: route_b
        }

        names_stops_a = response['Trips']['StopNamesA']
        names_stops_b = response['Trips']['StopNamesB']

        id_stopsA = [stop_id['Id'] for stop_id in response['Trips']['StopsA']]
        id_stopsB = [stop_id['Id'] for stop_id in response['Trips']['StopsB']]

        return directions, names_stops_a, names_stops_b, id_stopsA, id_stopsB


    def schedule_for_stop(self, bus_route, stop, direction):
        data = {
            'p':'minsk',
            'tt':'bus',
            'r':bus_route,
            's':stop,
            'd':direction,
            '__RequestVerificationToken':'oSuEC7bISPi0b3LmD2Z7fKZ1FI2ZGXl3cMwpV18n4avmS146x-nc5nvuVPqYk760HqJHg_Y50SZ16v92SFm2vy0lgWk6n3SzvGIp2rMk0Yg1',
        }

        response = requests.post('https://www.minsktrans.by/lookout_yard/Data/Schedule', cookies=self.cookies, headers=self.headers,
                                 data=data).json()

        try:
            schedule_by_hours = response['Schedule']['HourLines']

        except:
            schedule_by_hours = response['DaysOfWeek'][0]['HourLines']

        hours_minutes = ''
        for schedule in schedule_by_hours:
            hours_minutes = hours_minutes + f"Час: {schedule['Hour']} Минуты: {schedule['Minutes']}\n"

        return zip([schedule['Hour'] for schedule in schedule_by_hours], [schedule['Minutes'] for schedule in schedule_by_hours])