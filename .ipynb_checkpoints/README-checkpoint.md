<a name="readme-top"></a>

# Indian-News-Channel-Toxicity

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

In response to the dynamic landscape of digital media, our research project centers on the changing nature of news debates on Indian channels. As traditional media adapts to the digital era, online platforms now constitute 43% of registered channels, reaching an audience of 450 million as of 2020. This transition, however, has raised concerns about the escalating levels of aggression, toxicity, and biases within news debates.

Our project aims to provide a comprehensive understanding of the evolution of debates on national and regional news channels over the past decade. Fueled by factors such as privatization, deregulation, and external pressures, these debates have devolved into contentious discussions, blurring the lines between informative discourse and sensationalism. We seek to uncover the social consequences of these intense conversations marked by heated arguments and confrontations.

Distinguishing itself from existing research, our project pioneers an exploration into the toxicity levels of online and cable network news debates. This focus arises from the high viewership of these debates and their potential to cause harm. Additionally, we address the challenge of limited datasets for analysis by leveraging advanced natural language processing techniques to gain deeper insights.

Beyond immediate concerns of news content, our research aims to contribute to social and behavioral understanding. By unraveling imbalances and deliberate intentions in communication, we seek to expose the motivations behind organizing controversial debates, the role of government in content regulation, and the cultivation of extreme public opinions. The findings are anticipated to inform advancements in NLP algorithms, influencing content moderation, bias detection, and the spread of influence in prime-time debates.

In conclusion, our project delves into the intricacies of news debates in the digital age, offering valuable insights to foster responsible journalism and promote societal well-being. Through this exploration, we aim to contribute to shaping a more informed and balanced media landscape for the future.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

As a prerequisite, you should make sure you have Python3 installed. 

### Installation

This section covers different packages you would be needing to get the code running locally.

1. Get your API key from [Youtube Developer Website](https://developers.google.com/youtube). 
2. Install packages
   ```sh
   pip3 install scrapetube
   pip3 install pandas
   pip3 install google-api-python-client
   ```
4. Enter your API in `Video ID Generator.ipynb`
   ```sh
   os.environ["YOUTUBE_API_KEY"] = "API KEY"
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

For running the code locally, once you have completed the steps above, just clone the repository to your computer and run the required ipython notebook.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Gather video IDs for prime-time debates.
- [ ] Download the videos using the video ID and [YoutubeDL](https://github.com/ytdl-org/youtube-dl).
- [ ] Transcribe the videos to text using Whisper API. 
- [ ] Perform initial analysis on the data gathered.
- [ ] Use Large Language Models to detect toxicity.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
