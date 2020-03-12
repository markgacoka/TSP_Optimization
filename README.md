<p align="center">
    <img width="200" src="https://github.com/markgacoka/TSP_Optimization/blob/master/logo.png">
</p>

[![Logo](https://github.com/markgacoka/TSP_Optimization/blob/master/logo.png)]

<h1 align="center">TSP_Optimization</h1>
<div align="center">
An optimization solution to the Traveling Salesman Problem
**Optimization Problem**: To prevent the spread of an infectious disease, a vaccine needs to be distributed as quickly and efficiently as possible to the 15 cities that have had major outbreaks. How can you optimize the route between the cities?. 

[![Testing](https://github.com/markgacoka/TrashClassifier/blob/master/images/badge.svg)](https://github.com/markgacoka/TrashClassifier/issues)
</div>

[![Solution](https://github.com/markgacoka/TSP_Optimization/blob/master/solution.png)]

## Technical Details
#### Scenario 1 - Problem Statement: 

The objective function is to find the shortest route that the transporter could use to deliver the vaccine.
   
For all visited cities $\mathit{N}$ that are indexed from {$\mathit{0...N}$} and given a pair of cities, $a$ and $b$, and the distance between them c(a, b), the objective function is represented as: $min \sum a \sum b \hspace{0.3cm} c_{a,b} y_{a,b}$, $y$ being the cost to visit the respective city. This means that the objective function is optimized to minimize the total distance to be covered by the transporter.

- The cities represented in this problem statement corresponds to 15 locations affected by the Ebola virus in Liberia 2014. I converted the city coordinates from geodetic coordinate system to cartesian coordinate system then scaled from 1-10 and plotted in a graph.

Since the position of the coordinates and distance between them stay constant, our decision variable will be the order in which the cities are visited and is represented by the permutation cost for traveling all the cities $min \sum y_{a, b}$. By changing the order of routes to a feasible set of alternatives, we can either increase or decrease the value of the objective function which is the length of the path to be used. 

##### The constraints include:
1. **Go to constraint** - After visiting a city $N_i$, the transporter must visit only visit one city next.
2. **Come from constraint** - when visiting a city $N_i$, the transporter can only come from one city $N_{i-1}$.
3. **1-1 connection** - The cities should be fully connected with no sub-tours or according to graph theory, a hub with multiple nodes.
4. **Double visitation** - The transporter can not visit a city twice.

##### Assumptions:
1. The transporter goes back to the initial city for restocking.
2. There are no unaffected cities that connect the affected cities to form a shorter path.

##### Interpretation and Efficiency
The results indicate that the program is efficient in finding the global minimum when given enough time. I could further make it better by making the converged minimum distance be the stopping criteria instead of time. By jumping to random cities, running time could be cut short before the global optimum is found. Moreover, the program is not algorithmically efficient as a single execution of 3-opt local search has a time complexity of $O(N^3)$ and iterated 3-opt local search has higher time complexity.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on localhost. You can also check out the website [here](http://trashier.appspot.com/). If that does not work, you can check the layout without API calls to Houndify API [here](https://treehacks.netlify.com/).

### Prerequisites

What things you need to install the software and how to install them:
* npm
* git
* express-js

### Installing

To install the files to your computer, use git to clone the repository

[![Tutorial Video](https://github.com/markgacoka/TrashClassifier/blob/master/images/git-clone.gif)](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)


#### For Windows
Download [Git for Windows](https://gitforwindows.org/) if you don't have one already.

```
git --version
git config --global user.name "YOUR-NAME"
git config --global user.email "YOUR-EMAIL"
cd Desktop/
git clone https://github.com/markgacoka/TrashClassifier.git
```

#### For Mac
Use the first code to check if you have it installed.

```
git --version
git config --global user.name "YOUR-NAME"
git config --global user.email "YOUR-EMAIL"
brew install git
mkdir TrashClassifier/
git clone https://github.com/markgacoka/TrashClassifier
```

## Running the tests

Once downloaded to your local machine, you can go into the directory and test out the index file on your browser.

```
cd TrashClassifier/
index.html
```

## Deployment

However, the website is hosted by a nodeJS server and to do this you need to install npm.
1. Check if a nodeJS and npm are installed

```
node -v
npm -v
```

2. Install the latest version of npm and install expressJS using npm
```
npm install npm@latest -g
npm init
npm install express --save
node server.js
```

[![Node Server](https://github.com/markgacoka/TrashClassifier/blob/master/images/node-server.gif)](https://deploybot.com/blog/guest-post-how-to-set-up-and-deploy-nodejs-express-application-for-production)

## Built With

* [Teachable Machine by Google](https://teachablemachine.withgoogle.com/)
* [Google Cloud Storage Services](https://cloud.google.com/gcp/getting-started)
* [NodeJS](https://nodejs.org/en/docs/)
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [HTML & CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

## Versioning

This is the alpha version for the project. V 1.0.0.
To see Trung's version of the project during the hackathon, [click here](https://treehacks-trashier.appspot.com/).

## Authors
<table>
  <tr>
    <td align="center"><a href="https://github.com/markgacoka"><img src="https://avatars2.githubusercontent.com/u/23658445?s=460&v=4" width="100px;" alt=""/><br /><sub><b>Gacoka Mbui</b></sub></a><br /><a href="https://github.com/markgacoka/SafePath" title="Backend and Documentation">📖💻🤔</a></td>
    <td align="center"><a href="https://github.com/Nguyen-ATrung"><img src="https://avatars2.githubusercontent.com/u/55957585?s=460&v=4" width="100px;" alt=""/><br /><sub><b>Trung Nguyen</b></sub></a><br /><a href="https://github.com/Nguyen-ATrung/Treehacks" title="Front End, Marketing and Design">🐛🎨💻</a></td>
  </tr>
</table>

<div>
  <h2>Safe Path</h2>
  <p>A web app that displays the shortest safe path between two points in a map. Created using Django and Javascript.</p>
</div>

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- **[Creative Commons Attribution 3.0 License - (CC BY 3.0)](https://colorlib.com/wp/template/imagine/)**

## Acknowledgments
* TreeHacks Judges for the feedback on the code and the overall project.
* TreeHacks mentors for helping us when stuck.

Submitted to [TreeHacks 2020](https://devpost.com/software/trashier) at Stanford.


