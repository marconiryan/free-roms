from requests_html import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class HtmlContent:
    def __init__(self, url: str):
        self.url = url
        self.session = HTMLSession()
        self.async_session = AsyncHTMLSession()
        self.request_html_response: HTMLResponse = None
        self.async_session.run(self._get_request)

    async def _get_request(self):
        self.request_html_response = self.session.get(self.url)

    def get_link(self):
        return self.request_html_response.html.links


def save_rom(link: dict, queue: list, saved: list):
    try:
        title_rom = iter(link)
        title_rom = next(title_rom)
        try:

            print(f"{bcolors.WARNING}(In queue) {len(queue)} {bcolors.ENDC}{bcolors.BOLD}{title_rom}")
            if title_rom not in queue and title_rom not in saved and len(queue) < 2:
                queue.append(title_rom)
                response = requests.get(URL + link[title_rom])
                with open("./roms/" + title_rom, "wb") as write_rom:
                    write_rom.write(response.content)
                    write_rom.flush()
                    print("aaaaaa")

                print(f"{bcolors.OKGREEN}(Saved){bcolors.ENDC} {bcolors.BOLD}{title_rom}")
                queue.remove(title_rom)
                saved.append(title_rom)
                link.pop(title_rom)

        except:
            print(f"{bcolors.FAIL}(Saved){bcolors.ENDC} {bcolors.BOLD}{title_rom}")
    except:
        return


queue_rom = []
saved_rom = []

URL = "https://archive.org/download/nointro.snes/"
html_content = HtmlContent(URL)

links: dict = {}

for i in html_content.request_html_response.html.find("a"):
    title = i.full_text
    if ".zip" in title or ".7z" in title:
        for j in i.links:
            links[title] = j
            break
print(f"{bcolors.OKCYAN}(Links saved)")
if __name__ == "__main__":
    link = iter(links)
    while len(links) > 0:
        save_rom(links,queue_rom, saved_rom)
