<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<div align="center">
  <a href="https://github.com/leyuskckiran1510/PyStatisticsSolver">
    <!--<img src="images/logo.png" alt="Logo" width="80" height="80">-->
  </a>

  <h1 align="center">PyStatisticsSolver</h1>

  <p align="center">
    A simple python automation tool to compute possible statistics calculation like means,median etc. for given photo of series of data(i.e individual series,diescrit series and continious series).
    <br />
    <a href="https://github.com/leyuskckiran1510/PyStatisticsSolver"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/leyuskckiran1510/PyStatisticsSolver">View Demo</a>
    ·
    <a href="https://github.com/leyuskckiran1510/PyStatisticsSolver/issues">Report Bug</a>
    ·
    <a href="https://github.com/leyuskckiran1510/PyStatisticsSolver/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://github.com/leyuskc/PyStatisticsSolver)-->

This is a simple project for automating the repetating calculation of statistical data in Class.
The main theme here is to take the picture of the statistical chart and this will dump all the data nicely and calculated . It only shows the calulated values not the steps/process. The final result are printed and the consecutative calculations like fx f(x-xbar) .. 

Of course, This will have it's own limitaion and drawbacks but it's mainly programmed for my environment and not keeping on mind for scalibilty and extension.But if you like the project and want to contribute I open to that if I like it and won't make the code base more junk.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

It is built with python without any ML/DL modules or frameworks as It uses free API's to do the heavy task. And the main reason to do so is that my potato PC can't handel the model training and waiting hours to train is kind of wastefull when their are free apis with enough api calls per month.But the Basics Moduel used are

* [![Python][python3]][pythonorg]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

So If you want to use it for yourself then here is how.

### Prerequisites

You must have installed python in the first place.If you dont have you can download from [![Python][python3]][pythonorg] .Or if you want to use terminal for Unix/Linux
* Debian
  ```sh
  sudo apt install python3
  ```
### Installation

_Now the packages installation and file setup part.Follow the step below and you should be goto go._

1. Get a free API Key at [OCR-SPACE](https://ocr.space/ocrapi/freekey).

    i.Go to Above link.

    ii.Register and you should get your API-KEY on mail once verifed.


2. Clone the repo
   ```sh
   git clone https://github.com/leyuskckiran1510/PyStatisticsSolver.git
   cd ./PyStatisticsSolver
   ```
   I assume you are in the code folder after this till to very end.
3. You Can create a virtual enviroment, If you like it clean or just follow next step.
    ```bash
    python -m venv virtual
    source ./virtual/bin/activate

    ```
###                 OR 
3. Install Pyhton packages 
   ```sh
   python -m pip install -r ./requirements.txt
   ```
4. Setting Up your ApiKey in `.env`
   ```js
   echo API_KEY='YOUR_API_KEY' > .env
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

It main use is for the lazy people who are bored to type the data in the Online Avilable Free Calculators and Stuff. Now using this you can just click the Photo , and run the app when prompt choose the image you want to use and sit back and relax while the free/slow api process the data and see the magic of data apperaing in the terminal. If you want to take it further you can also intregrate to excel to automate the whole exle process.

_For more examples, please refer to the [Documentation](https://github.com/leyuskckiran1510/PyStatisticsSolver)._

_A Example or simple usecase video may be uploaded to youtube if uploaded then you can click this link [Video](https://youtube.com/watch)_

1. Using Cli Verison 
   ```sh
   python ./main.py
   ```

 ###  OR
1. Before using Web Version you need to install aditional package as follow 
   ```sh
   python -m pip install -r ./web/requirements.txt
   ```
2. Using Web Version 
   ```sh
   python ./web/web.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] language Support
    - [+] English

See the [open issues](https://github.com/leyuskckiran1510/PyStatisticsSolver/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


Project Link: [Click ME](https://github.com/leyuskckiran1510/PyStatisticsSolver)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I used ChatGpt for some problems as it was faster for me to ask it then to fid the term and find the correct result aside the Ads.
And Also great thanks to ocr-space teams for providing free ocr api . Also thanks to [@othneildrew](https://github.com/othneildrew/Best-README-Template) for providing these readme template.

* [OCR-SPACE](https://ocr.space/)
* [ChatGPT](https://chat.openai.com/chat)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




[contributors-shield]: https://img.shields.io/github/contributors/leyuskckiran1510/PyStatisticsSolver.svg?style=for-the-badge
[contributors-url]: https://github.com/leyuskckiran1510/PyStatisticsSolver/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/leyuskckiran1510/PyStatisticsSolver.svg?style=for-the-badge
[forks-url]: https://github.com/leyuskckiran1510/PyStatisticsSolver/network/members
[stars-shield]: https://img.shields.io/github/stars/leyuskckiran1510/PyStatisticsSolver.svg?style=for-the-badge
[stars-url]: https://github.com/leyuskckiran1510/PyStatisticsSolver/stargazers
[issues-shield]: https://img.shields.io/github/issues/leyuskckiran1510/PyStatisticsSolver.svg?style=for-the-badge
[issues-url]: https://github.com/leyuskckiran1510/PyStatisticsSolver/issues
[license-shield]: https://img.shields.io/github/license/leyuskckiran1510/PyStatisticsSolver.svg?style=for-the-badge
[license-url]: https://github.com/leyuskckiran1510/PyStatisticsSolver/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/leyuskc
[product-screenshot]: images/screenshot.png
[python3]:https://img.shields.io/badge/python3-000000?style=for-the-badge&logo=python
[pythonorg]:https://python.org

