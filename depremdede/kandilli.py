import re, requests

'''
We remember with respect Ahmet Mete Işıkara
https://en.wikipedia.org/wiki/Ahmet_Mete_I%C5%9F%C4%B1kara

Deprem Dede - Kandilli
Author : Seckin ALAN <seckinalan@gmail.com>
Description : This library parse Kandilli Observatory,
RECENT EARTHQUAKES IN TURKEY pages.


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

PREREG  = "<pre>(.*?)</pre>"
EQREG   = "(^[0-9](.*)\r\n)"
INFREG  = "(\d+\.\d+\.\d+).*(\d+\:\d+\:\d+)\s*(\d+\.\d+)\s*(\d+\.\d+)\s*(\d+\."
INFREG += "\d+)\s*(\d+\.\d+|-\.-)\s*(\d+\.\d+|-\.-)\s*(\d+\.\d+|-\.-)\s*(.*\s"
INFREG += "\s)\s(.*)\r\n"

INFCOM  = re.compile(INFREG)

def earthquake():
    eqlist = []
    page = requests.get("http://www.koeri.boun.edu.tr/scripts/lst9.asp")

    for i in re.findall(EQREG,re.findall(
            PREREG, page.content.decode("cp1254"),re.DOTALL
            )[0], re.M):
        h=i[0]
        try:
            reg = INFCOM.match(h)
            eqlist.append({
                'date':reg.group(1),
                'hour':reg.group(2),
                'latitude':reg.group(3),
                'longitude':reg.group(4),
                'depth':reg.group(5),
                'magnitude': {
                    'md':reg.group(6),
                    'ml':reg.group(7),
                    'mw':reg.group(8),
                },
                'region':reg.group(9).strip(),
                'solution':reg.group(10),
                })
        except:
            print("err")

    return eqlist

if __name__ == "__main__":
    print(earthquake())
