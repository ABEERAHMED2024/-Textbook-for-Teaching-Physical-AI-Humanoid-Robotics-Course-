---
title: "Notation Guide: Mathematical Symbols & Conventions"
description: "Standard mathematical notation and symbols used throughout the Physical AI & Humanoid Robotics course"
keywords: ["notation", "mathematical symbols", "conventions", "mathematics", "robotics"]
sidebar_position: 2
sidebar_label: "Notation Guide"
estimated_time: 15
week: null
module: null
prerequisites: []
learning_objectives:
  - "Recognize and understand standard mathematical notation used in robotics"
  - "Apply consistent mathematical conventions in problem solving"
  - "Interpret mathematical expressions in course materials"
assessment_type: null
difficulty_level: "beginner"
capstone_component: null
---

# Notation Guide: Mathematical Symbols & Conventions

This guide defines the mathematical notation and symbols used throughout the Physical AI & Humanoid Robotics course. Consistent notation helps ensure clarity and understanding across all modules.

## Scalars, Vectors, and Matrices

| Symbol | Meaning | Example |
|--------|---------|---------|
| $a, b, c$ | Scalar quantities | $a = 5.2$ |
| $\vec{v}, \vec{w}$ | Vector quantities | $\vec{v} = [x, y, z]^T$ |
| $\mathbf{A}, \mathbf{B}$ | Matrix quantities | $\mathbf{R} \in \mathbb{R}^{3\times 3}$ |
| $\|\vec{v}\|$ or $\|\vec{v}\|_2$ | Euclidean norm of vector $\vec{v}$ | $\|\vec{v}\| = (x^2 + y^2 + z^2)^{1/2}$ |
| $\vec{v} \cdot \vec{w}$ | Dot product of vectors | $\vec{v} \cdot \vec{w} = |\vec{v}||\vec{w}|\cos(\theta)$ |
| $\vec{v} \times \vec{w}$ | Cross product of vectors | $\vec{v} \times \vec{w} = \vec{n}|\vec{v}||\vec{w}|\sin(\theta)$ |

## Sets and Spaces

| Symbol | Meaning | Example |
|--------|---------|---------|
| $\mathbb{R}$ | Set of real numbers | $x \in \mathbb{R}$ |
| $\mathbb{R}^n$ | n-dimensional real vector space | $\mathbf{x} \in \mathbb{R}^3$ |
| $\mathbb{R}^{m \times n}$ | Set of real matrices with m rows and n columns | $\mathbf{A} \in \mathbb{R}^{3 \times 4}$ |
| $\mathbb{S}^2$ | Unit sphere in 3D space | $\mathbf{r} \in \mathbb{S}^2$ if $|\mathbf{r}| = 1$ |
| $\mathbb{SO}(3)$ | Special Orthogonal group (3D rotations) | $\mathbf{R} \in \mathbb{SO}(3)$ |
| $\mathbb{SE}(3)$ | Special Euclidean group (3D rigid transformations) | $\mathbf{T} \in \mathbb{SE}(3)$ |
| $\cup$ | Set union | $A \cup B$ |
| $\cap$ | Set intersection | $A \cap B$ |
| $\in$ | Element of | $x \in \mathbb{R}$ |
| $\subset$ | Subset of | $\mathbb{R}^2 \subset \mathbb{R}^3$ |

## Kinematics and Dynamics

| Symbol | Meaning | Example |
|--------|---------|---------|
| $\theta$ | Joint angle | $\theta_1$ for first joint |
| $\dot{\theta}$ | Joint velocity | $\dot{\theta} = d\theta/dt$ |
| $\ddot{\theta}$ | Joint acceleration | $\ddot{\theta} = d^2\theta/dt^2$ |
| $\mathbf{q}$ | Joint configuration vector | $\mathbf{q} = [\theta_1, \theta_2, \theta_3]^T$ |
| $\mathbf{J}$ | Jacobian matrix | $\mathbf{v} = \mathbf{J}\dot{\mathbf{q}}$ |
| $\mathbf{p}$ | Position vector | $\mathbf{p} = [x, y, z]^T$ |
| $\mathbf{R}$ | Rotation matrix | $\mathbf{R} \in \mathbb{SO}(3)$ |
| $\mathbf{T}$ | Transformation matrix | $\mathbf{T} = [ \mathbf{R} \ \mathbf{p}; \ \mathbf{0}^T \ 1 ]$ |
| $\omega$ | Angular velocity vector | $\omega \in \mathbb{R}^3$ |
| $\mathbf{v}$ | Linear velocity vector | $\mathbf{v} = d\mathbf{p}/dt$ |

## Control and Optimization

| Symbol | Meaning | Example |
|--------|---------|---------|
| $u(t)$ | Control input at time $t$ | $u(t) = K(x_d - x(t))$ |
| $x(t)$ | System state at time $t$ | $\dot{x} = f(x, u)$ |
| $y(t)$ | System output at time $t$ | $y = h(x)$ |
| $J$ | Cost function | $J = \int_0^T (x^T Q x + u^T R u) dt$ |
| $\pi$ | Policy function | $u = \pi(x)$ |
| $\mathcal{L}$ | Lagrangian | $\mathcal{L} = T - V$ |
| $\nabla$ | Gradient operator | $\nabla f(x) = \partial f/\partial x$ |
| $\partial$ | Partial derivative | $\frac{\partial f}{\partial x}$ |
| $\int$ | Integral | $\int_a^b f(x) dx$ |
| $\sum$ | Summation | $\sum_{i=1}^n x_i$ |

## Probabilities and Statistics

| Symbol | Meaning | Example |
|--------|---------|---------|
| $P(A)$ | Probability of event $A$ | $P(\text{obstacle}) = 0.1$ |
| $P(A|B)$ | Conditional probability of $A$ given $B$ | $P(\text{success}|\text{calibrated})$ |
| $\mu$ | Mean or expected value | $\mu = E[X]$ |
| $\sigma^2$ | Variance | $\sigma^2 = E[(X-\mu)^2]$ |
| $\sigma$ | Standard deviation | $\sigma = \sqrt{\sigma^2}$ |
| $\mathcal{N}(\mu, \sigma^2)$ | Normal distribution | $X \sim \mathcal{N}(\mu, \sigma^2)$ |
| $\approx$ | Approximately equal | $x \approx 3.14$ |
| $\sim$ | Distributed according to | $X \sim \mathcal{N}(0, 1)$ |

## Time and Derivatives

| Symbol | Meaning | Example |
|--------|---------|---------|
| $t$ | Time variable | $x(t)$ position at time $t$ |
| $\dot{x}$ | First time derivative | $\dot{x} = dx/dt$ |
| $\ddot{x}$ | Second time derivative | $\ddot{x} = d^2x/dt^2$ |
| $\Delta t$ | Time step or interval | $\Delta t = t_{k+1} - t_k$ |
| $t_0$ | Initial time | $t_0 = 0$ |
| $t_f$ | Final time | $t_f = 10$ seconds |

## Common Functions and Operators

| Symbol | Meaning | Example |
|--------|---------|---------|
| $\sin, \cos, \tan$ | Trigonometric functions | $\sin(\theta)$ |
| $\exp(x)$ or $e^x$ | Exponential function | $\exp(-x^2)$ |
| $\log(x)$ | Natural logarithm | $\log(x)$ |
| $\log_{10}(x)$ | Base-10 logarithm | $\log_{10}(100) = 2$ |
| $\delta(t)$ | Dirac delta function | $\int_{-\infty}^{\infty} \delta(t) dt = 1$ |
| $\mathcal{F}$ | Fourier transform | $\mathcal{F}[f(t)]$ |
| $\mathcal{L}$ | Laplace transform | $\mathcal{L}[f(t)]$ |

## Robotics-Specific Notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| $^A\mathbf{v}$ | Vector $\mathbf{v}$ expressed in frame $A$ | $^A\mathbf{p}_{B}$ position of B in A |
| $^A\mathbf{R}_B$ | Rotation matrix from frame $B$ to frame $A$ | $\mathbf{p}^A = ^A\mathbf{R}_B \mathbf{p}^B$ |
| $^A\mathbf{T}_B$ | Transformation matrix from frame $B$ to frame $A$ | $\mathbf{p}^A = ^A\mathbf{T}_B \mathbf{p}^B$ |
| $m$ | Mass | $m = 5$ kg |
| $\mathbf{I}$ | Inertia tensor | $\mathbf{I} \in \mathbb{R}^{3 \times 3}$ |
| $g$ | Gravitational acceleration | $g = 9.81$ m/s² |

## Common Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| DoF | Degrees of Freedom |
| FK | Forward Kinematics |
| IK | Inverse Kinematics |
| CoM | Center of Mass |
| COM | Center of Mass (alternative) |
| CoM | Center of Moment (in some contexts) |
| MPC | Model Predictive Control |
| PID | Proportional-Integral-Derivative controller |
| SLAM | Simultaneous Localization and Mapping |
| VSLAM | Visual SLAM |
| LQR | Linear Quadratic Regulator |
| SE(3) | Special Euclidean Group in 3D |
| SO(3) | Special Orthogonal Group in 3D |
| URDF | Unified Robot Description Format |
| SDF | Simulation Description Format |

---

**Note**: This notation guide will be updated as new symbols and conventions are introduced in the course. Always refer to the context when interpreting mathematical expressions, as notation may occasionally vary based on specific applications or literature.