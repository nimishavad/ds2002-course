---
layout: default
title: DS2002 Data Science Systems
---
## Course Description

This course exposes students to the essential technical concepts and skills for designing and running data science workloads. Students will be equipped to select and manage computing environments and storage options large and small. They will also learn methods for software delivery, scaling for larger jobs, and the essential database models for data storage and data analysis. 

Students in this course will become much more familiar with the command-line interface, scripting and managing code, and creating/managing local and cloud-based resources. A central goal of the course is to equip students in the technical aspects of their later work in data science, so that students have a wide range of tools, techniques, and skills for processing a variety of workloads. 

## Getting Started

To get started with the course, please follow the **[Setup Instructions](setup.md)** to configure your development environment.

## Practice

Work through the **[Hands-on Exercises](exercises.md)** to practice and consolidate concepts introduced during class lectures and discussions. 

Each unit contains an "Advanced Concepts" section that allows you to dive deeper into a topic. **Note: Advanced concepts will not be covered in quizzes or labs.**

Check the end of each unit for links to additional resources for further exploration.

## Labs

Weekly labs are released with instructions on the **[course Canvas page](https://canvas.its.virginia.edu/courses/167598)**.

## Repository Management

### Updating Your Fork

To stay current with new releases from the course repository:

1. Add an upstream source (if not already added):
   ```bash
   git remote add upstream git@github.com:nmagee/ds2002-course.git
   ```

2. Fetch from the upstream branch:
   ```bash
   git fetch upstream
   ```

3. Merge your branch with the upstream branch:
   ```bash
   git merge upstream/main main
   ```

### Saving Your Changes

If you generate code, scripts, data files, etc. that you would like to keep, add, commit, and push the files back to **your** fork of the repository:

```bash
git add .
git commit -m "Some meaningful message"
git push origin main
```

Remember that changes you commit and push will be saved to **your** fork of the repository.

