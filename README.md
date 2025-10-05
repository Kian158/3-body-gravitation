## Newtonian Gravitation Simulations + Visualisations

The aim of this project was to simulate the famous 3 body problem of Newtonian gravitation. It's very easy to simulate two bodies, but there is a jump in complexity when another is added.
There are two sub-projects here:
- A two body simulation, created first and used as the base of the 3 problem
- A three body simulation, as promised
both of which being visualised with matplotlib

They both utilise numerical integration to model the differential equations: 

m**a** = (- GMm / x^2 ) **x**
where m is the mass of the body under influence, **a** is acceleration, G is the gravitational constant, M is the mass of the body exerting influence, and **x** is the position vector joining these

These two sub-projects differ in the implimentation:
- The first uses _Euler's method_:
  **v_new** = **v_old** + **a** *dt
  for a small step _dt_
  however for the second, this was not sufficient as the approximations deviate too far when a third body is added. The planets kept shooting off to infinity. Thus,
- The second uses _Velocity-Verlet_, which is basically Euler's with another term for increased accuracy:
  **v_new** = **v_old** + 0.5*(**a_old** + **a_new**)  *dt
  Euler's method was taught on my university course, but I had to research this improvement after staring at wrong results for a long time.

## Results

Here are some interesting visualisations produced by playing with the initial conditions:
<img width="411" height="391" alt="grav5" src="https://github.com/user-attachments/assets/3d4577f0-9650-4aab-ba35-fb9c09c13e80" />
<img width="414" height="390" alt="grav1" src="https://github.com/user-attachments/assets/a1eebf21-d58e-4a8d-a121-f23ba57fdbe7" />
<img width="414" height="398" alt="grav2" src="https://github.com/user-attachments/assets/2b1d8c3c-7392-44f2-b943-662988d3d1e3" />
<img width="414" height="397" alt="grav3" src="https://github.com/user-attachments/assets/5c40c889-6d7d-4a87-b53f-6b465fe680eb" />


In the future I intend to extend this to N bodies
