import argparse
import json
import re
from datetime import datetime

def convert_cookie_to_json(cookie_data):
    # Split individual cookies by looking for "Cookie Key: " as a delimiter.
    cookies = re.split(r"(?<=Cookie Key: )", cookie_data)[1:]  # Ignore the first empty part if present

    cookie_list = []

    for idx, cookie in enumerate(cookies, start=1):
        print(f"Processing cookie #{idx}...")
        try:
            # Split cookie into lines and remove extra spaces
            lines = [line.strip() for line in cookie.strip().split("\n") if line.strip()]
            domain, path, secure, http_only, name, value, expiration_time = "", "", False, False, "", "", None

            for line in lines:
                print(f"Processing line: {line}")
                if line.lower().startswith("domain:"):
                    domain = line.split(": ", 1)[1].strip()
                elif line.lower().startswith("path:"):
                    path = line.split(": ", 1)[1].strip()
                elif line.lower().startswith("secure:"):
                    secure = line.split(": ", 1)[1].strip().lower() == "true"
                elif line.lower().startswith("httponly:"):
                    http_only = line.split(": ", 1)[1].strip().lower() == "true"
                elif line.lower().startswith("name:"):
                    name = line.split(": ", 1)[1].strip()
                elif line.lower().startswith("value:"):
                    value = line.split(": ", 1)[1].strip()
                elif line.lower().startswith("expiration time:"):
                    expiration_time = line.split(": ", 1)[1].strip()

            # Convert expiration_time to UNIX timestamp if possible
            if expiration_time:
                try:
                    expiration_time = datetime.strptime(expiration_time, "%Y-%m-%d %H:%M:%S").timestamp()
                except ValueError:
                    expiration_time = None

            # Skip cookies missing required fields
            if not name or not value:
                print(f"Skipping cookie #{idx}: Missing name or value.")
                continue

            # Add the parsed cookie data to our list
            cookie_list.append({
                "domain": domain,
                "path": path,
                "secure": secure,
                "httpOnly": http_only,
                "name": name,
                "value": value,
                "expirationDate": expiration_time
            })
            print(f"Successfully processed cookie #{idx}.")
        except Exception as e:
            print(f"Error parsing cookie #{idx}: {e}")

    # Return the JSON string
    return json.dumps(cookie_list, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Convert cookie data to JSON format.")
    parser.add_argument("-file", "--file", required=True, help="The input text file containing cookie data.")
    args = parser.parse_args()

    # Read the input file
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            cookie_data = f.read()
    except Exception as e:
        print(f"Error reading file {args.file}: {e}")
        return

    # Convert the cookie data to JSON
    json_output = convert_cookie_to_json(cookie_data)

    # Save the JSON output to cookies.json
    try:
        with open("cookies.json", "w", encoding="utf-8") as file:
            file.write(json_output)
        print("JSON conversion complete! Saved to cookies.json.")
    except Exception as e:
        print(f"Error writing to cookies.json: {e}")

if __name__ == "__main__":
    main()

