# Google Cloud Skill Boost Badge Counter

This Python project aims to count the number of GCP Skill Boost Badges in a public Google Cloud Skill Boost profile. It utilizes web scraping techniques to extract badge information from the provided profile URL.

## How it Works

1. **Fetch Webpage**: The program sends a request to the provided URL using the `requests` library to retrieve the HTML content of the webpage.

2. **Parse HTML**: Using BeautifulSoup from the `bs4` library, the HTML content is parsed to extract relevant information.

3. **Extract Badge Information**: The program identifies badge elements within the HTML structure based on their class name (`profile-badge`).

4. **Count Badges**: The number of badge elements found is counted to determine the total number of skill badges.

5. **Output Result**: The total number of skill badges is printed as output.

## Usage

To use this program:

### Prerequisites

Ensure you have the following prerequisites installed on your system:

- Python 3.x
- `requests` library: You can install it using `pip install requests`.
- `beautifulsoup4` library: You can install it using `pip install beautifulsoup4`.

### Getting Started

1. Clone the repository to your local machine:

```bash
git clone https://github.com/muhammedazhar/GCP-BadgeCounter
```

2. Navigate to the project directory:

```bash
cd GCP-BadgeCounter
```

3. Update the `url` variable in the script (`badge_counter.py`) with your personal public link to your Google Cloud Skill Boost profile.

4. Run the Python script:

```bash
python badge_counter.py
```

## Future Enhancements

Future enhancements planned for this project include:

- Providing details about the types and categories of badges.
- Improving the user interface for better interaction.
- Adding support for extracting additional information from the profile.

Feel free to contribute to this project or suggest any improvements!

## License

This project is licensed under the [MIT License](../docs/LICENSE).

## Questions and Support

If you have any questions or need support, feel free to open an issue or reach out to [Muhammed Azhar](https://github.com/muhammedazhar).

If you want to contribute to this project please read the [code of conduct](./docs/CODE_OF_CONDUCT.md) policy.

Happy coding!

---

*Note: This project is created to simplify the task of counting GCP Skill Boost Badges and is not affiliated with Google Cloud or the Skill Boost program.*