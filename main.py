import requests
from urllib.parse import urlparse
import re
import time

# Replace with your own Programmable Search Engine ID and API key
cse_id = "XXXXXXXXXXXXXXXXX"
api_key = "XXXXXXXXXXX_XXXXXXXXXXXX-XXXXXXXXXXXXXXXX"

def google_search(search_term, api_key, cse_id, **kwargs):
    service_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
    }
    params.update(kwargs)
    while True:
        response = requests.get(service_url, params=params)
        response_json = response.json()
        if 'error' in response_json:
            if response_json['error']['code'] == 429:
#                 print("Quota exceeded, waiting and retrying...")
                time.sleep(60)
                continue
            else:
                print(f"Error executing search: {response_json['error']}")
        return response_json

def get_school_url(school_name):
    query = school_name + " medical school"
    search_result = google_search(query, api_key, cse_id)
    if search_result.get('items'):
        url = search_result['items'][0]['link']
        netloc = urlparse(url).netloc
        return netloc.replace("www.", "")
    return None

def get_n_results(query):
    search_result = google_search(query, api_key, cse_id)
    return search_result['searchInformation']['totalResults']

schools = ["Albert Einstein College of Medicine",
"Anne Burnett Marion School of Medicine at TCU",
"Boston University Aram V. Chobanian & Edward Avedisian School of Medicine",
"Brody School of Medicine at East Carolina University",
"California Northstate University College of Medicine",
"California University of Science and Medicine",
"Carle Illinois College of Medicine",
"Case Western Reserve University School of Medicine",
"Central Michigan University College of Medicine",
"Charles E. Schmidt College of Medicine at Florida Atlantic University",
"Charles R. Drew University Of Medicine and Science College of Medicine",
"Chicago Medical School at Rosalind Franklin University of Medicine & Science",
"Columbia University Vagelos College of Physicians and Surgeons",
"Cooper Medical School of Rowan University",
"Creighton University School of Medicine",
"Donald and Barbara Zucker School of Medicine at Hofstra/Northwell",
"Drexel University College of Medicine",
"Duke University School of Medicine",
"East Tennessee State University James H. Quillen College of Medicine",
"Eastern Virginia Medical School",
"Emory University School of Medicine",
"Florida International University Herbert Wertheim College of Medicine",
"Florida State University College of Medicine",
"Frank H. Netter MD School of Medicine at Quinnipiac University",
"Frederick P. Whiddon College of Medicine at the University of South Alabama",
"Geisel School of Medicine at Dartmouth",
"Geisinger Commonwealth School of Medicine",
"George Washington University School of Medicine and Health Sciences",
"Georgetown University School of Medicine",
"Hackensack Meridian School of Medicine",
"Harvard Medical School",
"Howard University College of Medicine",
"Icahn School of Medicine at Mount Sinai",
"Indiana University School of Medicine",
"Jacobs School of Medicine and Biomedical Sciences at the University at Buffalo",
"Johns Hopkins University School of Medicine",
"Kaiser Permanente Bernard J. Tyson School of Medicine",
"Keck School of Medicine of the University of Southern California",
"Kirk Kerkorian School of Medicine at UNLV",
"Lewis Katz School of Medicine at Temple University",
"Loma Linda University School of Medicine",
"Louisiana State University School of Medicine in New Orleans",
"Louisiana State University School of Medicine in Shreveport",
"Loyola University Chicago Stritch School of Medicine",
"Marshall University Joan C. Edwards School of Medicine",
"Mayo Clinic Alix School of Medicine",
"Medical College of Georgia at Augusta University",
"Medical College of Wisconsin",
"Medical University of South Carolina College of Medicine",
"Meharry Medical College",
"Mercer University School of Medicine",
"Michigan State University College of Human Medicine",
"Morehouse School of Medicine",
"New York Medical College",
"Northeast Ohio Medical University",
"Northwestern University The Feinberg School of Medicine",
"Nova Southeastern University Dr. Kiran C. Patel College of Allopathic Medicine",
"NYU Grossman Long Island School of Medicine",
"NYU Grossman School of Medicine",
"Oakland University William Beaumont School of Medicine",
"Ohio State University College of Medicine",
"Oregon Health & Science University School of Medicine",
"Pennsylvania State University College of Medicine",
"Perelman School of Medicine at the University of Pennsylvania",
"Ponce Health Sciences University School of Medicine",
"Renaissance School of Medicine at Stony Brook University",
"Robert Larner",
"M.D.",
"College of Medicine at the University of Vermont",
"Rush Medical College of Rush University Medical Center",
"Rutgers New Jersey Medical School",
"Rutgers",
"Robert Wood Johnson Medical School",
"Saint Louis University School of Medicine",
"San Juan Bautista School of Medicine",
"Sidney Kimmel Medical College at Thomas Jefferson University",
"Southern Illinois University School of Medicine",
"Spencer Fox Eccles School of Medicine at the University of Utah",
"Stanford University School of Medicine",
"State University of New York Upstate Medical University Alan and Marlene Norton College of Medicine",
"SUNY Downstate Health Sciences University College of Medicine",
"The University of Toledo College of Medicine and Life Sciences",
"The Warren Alpert Medical School of Brown University",
"Tufts University School of Medicine",
"Tulane University School of Medicine",
"Uniformed Services University of the Health Sciences F. Edward Hebert School of Medicine",
"Universidad Central del Caribe School of Medicine",
"University of Alabama at Birmingham Marnix E. Heersink School of Medicine",
"University of Arizona College of Medicine - Phoenix",
"University of Arizona College of Medicine ? Tucson",
"University of Arkansas for Medical Sciences College of Medicine",
"University of California",
"Davis",
"School of Medicine",
"University of California",
"Irvine",
"School of Medicine",
"University of California",
"Los Angeles David Geffen School of Medicine",
"niversity of California",
"Riverside School of Medicine",
"University of California",
"San Diego School of Medicine",
"niversity of California",
"San Francisco",
"School of Medicine",
"University of Central Florida College of Medicine",
"University of Chicago Division of the Biological Sciences The Pritzker School of Medicine",
"University of Cincinnati College of Medicine",
"University of Colorado School of Medicine",
"University of Connecticut School of Medicine",
"University of Florida College of Medicine",
"University of Hawaii",
"John A. Burns School of Medicine",
"University of Illinois College of Medicine",
"University of Iowa Roy J. and Lucille A. Carver College of Medicine",
"University of Kansas School of Medicine",
"University of Kentucky College of Medicine",
"University of Louisville School of Medicine",
"University of Maryland School of Medicine",
"University of Massachusetts T.H. Chan School of Medicine",
"University of Miami Leonard M. Miller School of Medicine",
"University of Michigan Medical School",
"University of Minnesota Medical School",
"University of Mississippi School of Medicine",
"University of Missouri-Columbia School of Medicine",
"University of Missouri-Kansas City School of Medicine",
"University of Nebraska College of Medicine",
"University of Nevada",
"Reno School of Medicine",
"University of New Mexico School of Medicine",
"University of North Carolina at Chapel Hill School of Medicine",
"University of North Dakota School of Medicine and Health Sciences",
"University of Oklahoma College of Medicine",
"University of Pittsburgh School of Medicine",
"University of Puerto Rico School of Medicine",
"University of Rochester School of Medicine and Dentistry",
"University of South Carolina School of Medicine Columbia",
"University of South Carolina School of Medicine Greenville",
"University of South Dakota",
"Sanford School of Medicine",
"University of Tennessee Health Science Center College of Medicine",
"University of Virginia School of Medicine",
"University of Washington School of Medicine",
"University of Wisconsin School of Medicine and Public Health",
"USF Health Morsani College of Medicine",
"Vanderbilt University School of Medicine",
"Virginia Commonwealth University School of Medicine",
"Virginia Tech Carilion School of Medicine",
"Wake Forest University School of Medicine",
"Washington State University Elson S. Floyd College of Medicine",
"Washington University in St. Louis School of Medicine",
"Wayne State University School of Medicine",
"Weill Cornell Medicine",
"West Virginia University School of Medicine",
"Western Michigan University Homer Stryker M.D. School of Medicine",
"Wright State University Boonshoft School of Medicine",
"Yale School of Medicine"
]
print("school,","school_url,","biomedical_count")
for school in schools:
    school_url = get_school_url(school)
    if school_url:
        query = f"\"biomedical informatics\" site:{school_url}"
        print(f"{school},{school_url},{get_n_results(query)}")
    else:
        print(f"Could not find URL for school: {school}")
