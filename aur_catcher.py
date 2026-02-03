import os 
import requests


def inputer(text, value=str):
    print(text)
    return value(input("    >>> "))

def get_pkg_info(pkg_name):
    url = f"https://aur.archlinux.org/rpc/?v=5&type=info&arg[]={pkg_name}"

    try:
        response= requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data.get("resultcount") > 0:
                pkg = data["results"][0]

                name = pkg.get("Name")

                version = pkg.get("Version")

                description = pkg.get("Description")

                website = pkg.get("URL")

                aur_path = "https://aur.archlinux.org"+ pkg.get("URLPath")

                num_votes = pkg.get("NumVotes", 0)

                pop = pkg.get("Popularity",0)

                if num_votes > 50 and pop > 1.0:
                    status = "Safe"
                elif num_votes >= 10:
                    status = "Likely Safe"
                else:
                    status = "Getting Sus - Check the PKGBUILD!"

                return (
                    f"\nName: {name}\n"
                    f"Version: {version}\n"
                    f"Description: {description}\n"
                    f"Website: {website}\n"
                    f"Snapshot: {aur_path}\n"
                    f"Votes: {num_votes}\n"
                    f"Popularity: {pop}\n"
                    f"Status: {status}\n"
                )
            else:
                return f"Error: Package '{pkg_name}' not found"
        else:
            return f"Error: Server return status code {response.status_code}"
    
    except Exception as e:
        return f"an unexpected error! , {e}"


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        target_pkg = inputer("Enter the AUR package name").strip()
        print(get_pkg_info(target_pkg))
        input("Press Enter to continue...")
        
