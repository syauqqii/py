from requests import get
from json import loads
from os import system
from argparse import ArgumentParser

BASE_URL = "https://apim-bm7-prod-web.azure-api.net"
FORMAT_URL_0 = "{}/func-bm7-profile-prod/UserProfile"
FORMAT_URL_1 = "{}/func-bm7-course-prod/ClassSession/Upcoming/student"
FORMAT_URL_2 = "{}/func-bm7-course-prod/ClassSession/Session/{}/Resource/Student?isWeb=true"

def main(JWT_TOKEN):
	system("cls||clear")

	HEADERS = {
	    "Host": "apim-bm7-prod-web.azure-api.net",
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
	    "Accept": "application/json, text/plain, */*",
	    "Accept-Language": "en-US,en;q=0.5",
	    "Accept-Encoding": "gzip, deflate, br",
	    "Content-Type": "application/json",
	    "Authorization": f"Bearer {JWT_TOKEN}",
	    "Origin": "https://newbinusmaya.binus.ac.id",
	    "Connection": "keep-alive",
	    "Referer": "https://newbinusmaya.binus.ac.id/",
	    "Sec-Fetch-Dest": "empty",
	    "Sec-Fetch-Mode": "cors",
	    "Sec-Fetch-Site": "cross-site"
	}

	response = get(FORMAT_URL_0.format(BASE_URL), headers=HEADERS)

	res = loads(response.text)["roleCategories"][0]["roles"][0]

	roleOrganizationId = res["roleOrganizationId"]
	academicCareer = res["academicCareer"]
	institution = res["institution"]
	roleName = res["name"]
	roleId = res["roleId"]

	HEADERS.update({
	    "Authorization": f"Bearer {JWT_TOKEN}",
	    "rOId": f"{roleOrganizationId}",
	    "academicCareer": f"{academicCareer}",
	    "institution": f"{institution}",
	    "roleName": f"{roleName}",
	    "roleId": f"{roleId}",
	})

	response = get(FORMAT_URL_1.format(BASE_URL), headers=HEADERS)

	res = loads(response.text)

	sessionId = res["sessionId"]
	courseName = res["courseName"]
	classCode = res["classCode"]
	classRoomNumber = res["classRoomNumber"]
	classDeliveryMode = res["classDeliveryMode"]
	deliveryModeDesc = res["deliveryModeDesc"]
	courseComponent = res["courseComponent"]
	institutionDesc = res["institutionDesc"]
	lecturer_name = res["lecturers"][0]["name"]
	date = res["dateStart"].split('T')[0]
	date_start = res["dateStart"].split('T')[1]
	date_end = res["dateEnd"].split('T')[1]

	print(f"\n > Course     : {courseComponent} - {courseName}")
	print(f"   Lecturer   : {lecturer_name}")
	print(f"   Class      : {classCode} - {classRoomNumber}")
	print(f"   Delivery   : {classDeliveryMode} - {deliveryModeDesc}")
	print(f"   Institute  : {institutionDesc}")
	print(f"   Date, Time : {date}, {date_start} - {date_end}")

	response = get(FORMAT_URL_2.format(BASE_URL, sessionId), headers=HEADERS)

	print(f"\n   Link Zoom  : {loads(response.text)["joinUrl"]}")

if __name__ == '__main__':
	try:
		parser = ArgumentParser(description='Get Zoom Link Binus')
		parser.add_argument('-T', '--token', dest='token', type=str, help='Masukkan JWT TOKEN anda')
		args = parser.parse_args()

		if args.token is None:
			print("\n > Jalankan: python main.py --token JWT_TOKEN")
			exit(1)
		else:
			main(args.token)
	except KeyboardInterrupt:
		exit(1)
