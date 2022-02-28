# Thruster Vector Drive Conventions

These are conventions that we have used to define the vector drive

<img src="https://i.imgur.com/d5XSnOQ.jpg" width="200">
The arrows denote the direction of the resulting force vector given a positive input. 

There are 6 degrees of motion: forward/backward, strafe left/right, up/down, pitch up/down, roll right-down/left-down, yaw cw/ccw.
Where the forward, right, up, up, right-down, and ccw are the positive directions for each respectively. 

Matrices in the form of:
[direction input] -> [value of motor]
<table>
  <tr>
    <td>F/B
    <td>
    <td> Motor 1
  </tr>
  <tr>
    <td>L/R
    <td>
    <td> Motor 2
  </tr>
  <tr>
    <td>U/D
    <td> ->
    <td> Motor 3
  </tr>
  <tr>
    <td>P
    <td>
    <td> Motor 4
  </tr>
  <tr>
    <td>R
    <td>
    <td> Motor 5
  </tr>
  <tr>
    <td>Y
    <td>
    <td> Motor 6
  </tr>
</table>


<div>

<table align=left>
 <tr>
   <th>Forward
  </tr>
 <tr>
    <td>1
    <td>
    <td> 1
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
  </tr>
  <tr>
    <td>0
    <td> ->
    <td> 1
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
  </tr>
  <tr>
    <td>0
    <td>
    <td>0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
</table>

<table align=left>
  <tr> 
    <th> Backward
  </tr>
 <tr>
    <td>-1
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td> ->
    <td> -1
  </tr>
  <tr>
    <td>0
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td>
    <td>0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
</table>
  
<table align=left>
  <tr> 
    <th> Right
  </tr>
 <tr>
    <td>0
    <td>
    <td> -1
  </tr>
  <tr>
    <td>1
    <td>
    <td> 1
  </tr>
  <tr>
    <td>0
    <td> ->
    <td> -1
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
  </tr>
  <tr>
    <td>0
    <td>
    <td>0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
</table>
  
<table align=left>
  <tr> 
    <th> Left
  </tr>
 <tr>
    <td>0
    <td>
    <td> 1
  </tr>
  <tr>
    <td>-1
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td> ->
    <td> 1
  </tr>
  <tr>
    <td>0
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td>
    <td>0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
</table>
  
  <table align=left>
  <tr> 
    <th> Up
  </tr>
 <tr>
    <td>0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>1
    <td> ->
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td>1
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
  </tr>
</table>
  
  <table>
  <tr> 
    <th> Down
  </tr>
 <tr>
    <td>0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>-1
    <td> ->
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td>-1
  </tr>
  <tr>
    <td>0
    <td>
    <td>-1
  </tr>
</table>
  
<table align=left>
  <tr> 
    <th> Pitch
  </tr>
 <tr>
    <td>0
    <td>
    <td> 0
    <td>
    <td> 0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
    <td>
    <td>0
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td> ->
    <td> 1
    <td>
    <td>0
    <td>->
    <td>-1
  </tr>
  <tr>
    <td>1
    <td>
    <td> 0
    <td>
    <td>-1
    <td>
    <td>0
  </tr>
  <tr>
    <td>0
    <td>
    <td>1
    <td>
    <td>0
    <td>
    <td>-1
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
    <td>
    <td>0
    <td>
    <td>-1
  </tr>
</table>
  
<table align="left">
  <tr> 
    <th> Roll
  </tr>
 <tr>
    <td>0
    <td>
    <td> 0
    <td>
    <td> 0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>0
    <td>
    <td>0
    <td>
    <td>0
    <td>
    <td> 0
  </tr>
  <tr>
    <td>0
    <td> ->
    <td> 0
    <td>
    <td>0
    <td>->
    <td>0
  </tr>
  <tr>
    <td>0
    <td>
    <td> 0
    <td>
    <td>0
    <td>
    <td>0
  </tr>
  <tr>
    <td>1
    <td>
    <td>-1
    <td>
    <td>-1
    <td>
    <td>1
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
    <td>
    <td>0
    <td>
    <td>-1
  </tr>
</table>
  
  <table align="left">
  <tr> 
    <th> Yaw
  </tr>
 <tr>
    <td>0
    <td>
    <td> 1
    <td>
    <td> 0
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td>
    <td> 1
    <td>
    <td>0
    <td>
    <td> -1
  </tr>
  <tr>
    <td>0
    <td> ->
    <td> -1
    <td>
    <td>0
    <td>->
    <td>1
  </tr>
  <tr>
    <td>0
    <td>
    <td>-1
    <td>
    <td>0
    <td>
    <td>1
  </tr>
  <tr>
    <td>0
    <td>
    <td>0
    <td>
    <td>0
    <td>
    <td>0
  </tr>
  <tr>
    <td>1
    <td>
    <td>0
    <td>
    <td>-1
    <td>
    <td>0
  </tr>
</table>
</div>

