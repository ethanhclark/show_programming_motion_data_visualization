# Show Programming Motion Data Visualization Tools
<p>Show programming tools for visualizing kinematic motion data for suspended dark ride system. Python scripts calculating RV distance traveled along track curve and vehicle velocity found under <strong>scripts</strong>, and a Blender scene with timing + rotation data visualizations created using geometry nodes in Blender 4.2 can be found under <strong>3D_files</strong>. </p>

![data-visualization](https://github.com/user-attachments/assets/b1b06759-563f-40f8-93c7-8fbd584a5002)

<h1>How to Use Timing + Rotation Visualization Tools</h1>
<em>For <strong>Total Ride Time</strong> visualization:</em>
<ul>
  <li>Click on the <strong>GN_scene-time</strong> object under the <strong>GeoNodes Data</strong> collection in the Outliner. Under the <strong>Geometry Nodes</strong> tab, the overall scene time is referenced and visualized in seconds.</li>
</ul>
<em>For RV <strong>Yaw</strong> and <strong>Roll</strong> rotation visualization:</em>
<ul>
   <li>Click on the corresponding geometry node object in the 3D viewport and navigate to the <strong>Geometry Nodes</strong> tab. Under the <strong>Object Info</strong> node, the referenced object can be modified to correspond to appropriate rotation controller for rigged RV (see figure below).</li>
</ul>

<img width="2886" alt="export-filepath" src="https://github.com/user-attachments/assets/9c733904-f33c-4692-9333-46c1a01d9be9">

<h1>How to Use Distance + Velocity Visualization Tools</h1>
<em>For Calculating RV Distance along track curve:</em>
<ul>
  <li>Under the <strong>Scripting</strong> tab, open up the <strong>distance-property.py</strong> file from the <strong>scripts</strong> folder.</li>
  <li>On line 41, replace <strong>"track-curve"</strong> with the name of your track curve with desired path animation created (see figure below).</li>
  <li>Click the <strong>Run Script</strong> button (play button)</li>
  <li>A new cube called <strong>Traveled_Distance_Cube</strong> is created at the world origin and moves along the x-axis according to the distance of your RV along the track curve. This object is referenced in the geometry node setup for <strong>GN_distance</strong> object under the <strong>GeoNodes Data</strong> collection in the Outliner.</li>
</ul>

![distance-visualization](https://github.com/user-attachments/assets/9f5277e7-044b-4955-9c98-58927512b7e0)


<em>For Calculating RV velocity along track curve:</em>
<ul>
  <li>First complete the above steps for calculating RV distance along track curve.</li>
  <li>Under the <strong>Scripting</strong> tab, open up the <strong>velocity-property.py</strong> file from the <strong>scripts</strong> folder.</li>
  <li>On line 40, replace <strong>"track-curve"</strong> with the name of your track curve with desired path animation created (see figure below).</li>
  <li>Click the <strong>Run Script</strong> button (play button)</li>
  <li>A new cube called <strong>Traveled_Distance_Cube_Lagged</strong> is created at the world origin and is referenced in the geometry node setup for <strong>GN_velocity</strong> object under the <strong>GeoNodes Data</strong> collection in the Outliner.</li>
</ul>

![velocity-visualization](https://github.com/user-attachments/assets/276b0d5b-4a26-4859-b27f-3059c656eaad)
