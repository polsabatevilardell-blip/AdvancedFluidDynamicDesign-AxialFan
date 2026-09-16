# Advanced Fluid Dynamic Design
## Axial Fan

Welcome to the subject **Advanced Fluid Dynamic Design** (AFD). This course will cover the design and testing of an **axial fan** from three engineering point of views: 
Theoretical estimation (properly _Design_), numerical computation (_CFD_ Computational Fluid Dynamics) and Experimental testing (_Experimental_)

The course is prepared according to Project-Based Learning methodology.

## Objectives

The main objectives of using the PBL methodology are:

1. Learning to **work in group**, with specialized roles
2. Learn to make **autonomous work** and **effective research**
3. Learn to apply practical knowledge of **Fluid Mechanics, CFD and Experimental Methods**

## Methodology

The project is made by groups that are going to be generated in the present session. Each group is composed by 3–4 students. Each
student is assigned with a specific role:

- Student _expert in CFD_
- Student _expert in Experimentation_
- Students (1-2) _experts in Design_. Also, will be the leader and team representative in front of the teachers

The groups are generated in classroom, in the proper application in **Atenea**.

The activities will be of three types: 

1. **Individual work.** Each student will study and work the topics, with special focus on its expertise field 

![Individual work](images/P1_individual_work.png)

2. **Group work.** The group will meet, ideally every week, and collect all the information provided by each expert. In this meeting the taks are distributed, and decisions have to be made. The information of these meetings will be posted in a logbook

![Group work](images/P1_group_work.png)

3. **Experts meetings.** In classroom, groups are decomposed and each expert meets his/her counterparts of the other groups. The share experiences, problems, solutions and learn from each other.

![Experts meetings](images/P1_experts_meetings.png)

- The **Constitutive Minute:** The very first document where the following information will be detailed:
  - Team number
  - Team members
  - Roles
  - Project title and a brief description
  - Team's work regulations
- The **logbook:** A document with information of all the team meetings:
  - Date and hour
  - Attendants
  - Notes
  - Tasks
- The **Project report.** The main document. It will include all the information about the three aspects of the project: Design, CFD and Experimentation. There will be three releases to be submitted.
  - **Release 0.** A very basic version with the description of the fan
    - dimensions
    - performance
    - estimated power consumption
    - applications
    - examples from the web (at least three)
  - **Release 1.** A more detailed version with 
    - some design computations (mean line analysis) and first estimation of the performance
    - Preliminary numerical simulation of the mean line analysis
    - Proposal of experimental instrumentation and test bench design according to the ISO
    - Some bibliography
  - **Release 2.** Definitive version with the definitive design of the fan, CFD and test bench design and User Guide.

Note that the Project report are not three different documents, but **3 versions (releases) of the same document**.

In the last session all the teams will make a small presentation (10–15 minutes) of the project report. No need to make a presentation document, it can be made with the same Release 2 of the report, posted in the GitHub repository.

Also, there will be an **individual exam** at the end of the course with 
questions about the content of the three modules of the course

## Planning

The specific planning will be published in Atenea, but an overall version is shown here


| Task | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:--:|:--:|:--:|
| Presentation & kick-off | ██ | | | | | | | | | | | | |
| **Design** | | | | | | | | | | | | | |
| D1 Fundamentals | | ██ | | | | | | | | | | | |
| D2 Mean line analysis | | | | ██ | | | | | | | | | |
| D3 Radial equilibrium | | | | | | ██ | | | | | | | |
| D4 Blade and rotor design | | | | | | | | ██ | | | | | |
| D5 Final remarks | | | | | | | | | | ██ | | | |
| **CFD** | | | | | | | | | | | | | |
| C1 SimScale & first simulation | | | ██ | | | | | | | | | | |
| C2 Boundary layer and GCI | | | | | ██ | | | | | | | | |
| C3 Aerodynamics of an airfoil | | | | | | | ██ | | | | | | |
| C4 Simulation of axial fan | | | | | | | | | ██ | | | | |
| C5 Post-processing | | | | | | | | | | | ██ | | |
| **Experimental** | | | | | | | | | | | | | |
| E1 Measurement of magnitudes | | ██ | | | | | | | | | | | |
| E2 Error management | | | | ██ | | | | | | | | | |
| E3 ISO 5801:2019 | | | | | | ██ | | | | | | | |
| E4 Airfoil aerodynamics | | | | | | | | ██ | | | | | |
| E5 Fan testing in lab | | | | | | | | | | ██ | | | |
| E6 Testbench design | | | | | | | | | | | | ██ | |
| **Milestones** | | | | | | | | | | | | | |
| ⭐ Expert Meeting 1 | | | ⭐ | | | | | | | | | | |
| ⭐ Expert Meeting 2 | | | | | | | ⭐ | | | | | | |
| ⭐ Expert Meeting 3 | | | | | | | | | | | ⭐ | | |
| 🏷️ Release 0 | | | | 🏷️ | | | | | | | | | |
| 🏷️ Release 1 | | | | | | | | 🏷️ | | | | | |
| 🏷️ Release 2 | | | | | | | | | | | | 🏷️ | |
| 🎯 Presentations & exam | | | | | | | | | | | | | 🎯 |



## Grading

The grading is more detailed in the [course guide](https://eseiaat.upc.edu/en/programmes/industrial-engineering/masters-degree-in-industrial-engineering/curriculum/curriculum-muei-2025?set_language=en).

A brief summary of the weights is:

| Topic | Weight |
|-------|--------|
| Project report r0 | 15% |
| Project report r1 | 20% |
| Project report r2 | 30% |
| Presentation | 10% |
| Exam | 25% |

A co-evaluation factor $F \in (0.75,1.25)$ will be computed for each component of the groups from anonymous inquiry, in order to reward the most contributive members, and avoid the free-riders. This factor $F$ will modify only the 65% part related to the project report.

That is, the grade of each student will be computed with the equation

$$
\text{Grade} = \left(G_{r0}\times0.15 + G_{r1}\times0.20 + G_{r2}\times0.30  \right)\times F + G_{pr}\times 0.1 + G_{ex}\times 0.25
$$

of course, with a maximum of 10/10.


## Quality criteria

The report releases have to fulfill the following quality criteria:

### Release 0
  1. Role assignments
  2. Specifications of the axial fan of the project
  3. Group regulations
  4. Applications
  5. Examples (at least 3)

### Design

#### Release 1
1. Specification and dimensionless parameters
2. Geometry description of all the parts of the axial fan
3. Materials and characteristics. Justification
4. Mean line analysis
#### Release 2
5. Radial analysis
6. Mean line corrections
7. Blade and rotor design
8. Overall expected performance

### CFD

#### Release 1
1. CAD description
2. Mesh description
3. Boundary conditions
#### Release 2
4. Turbulence models. $y^+$ analysis
5. GCI
6. Post-process. Performance curves

### Experimentation

#### Release 1
1. Relevant variables of the axial fan
2. Proposed instrumentation for measuring and data acquisition
3. ISO 5801:2019 application to the axial fan
#### Release 2
4. Errors identification and propagation
5. Design of test bench and User's Guide.


## Tasks

The following tasks have to be done in this first session:

 - [ ] Generate groups in Atenea
 - [ ] Create a [GitHub account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) with the UPC mail, if you don't have already it.
 - [ ] Read documentation for Git and GitHub in the [GitHub training website](https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources)
 - [ ] Leader: Use the [Project Template](https://github.com/UPC-Fluid-Mechanics/AxialFan-Project-Template) to create your own repository and invite the rest of the team as collaborators.
 - [ ] Create a clone of the new repository in your local computer
 - [ ] If you don't have a preferred code editor, Visual Studio Code is recommended. [Install it](https://docs.github.com/en/get-started/git-basics/associating-text-editors-with-git).

Farem una prova a veure si es veu el text



