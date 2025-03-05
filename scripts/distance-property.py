import bpy

# Function to get the length of the curve
def get_curve_length(curve_obj):
    """Calculate the total length of a curve."""
    depsgraph = bpy.context.evaluated_depsgraph_get()
    evaluated_curve = curve_obj.evaluated_get(depsgraph)
    
    if evaluated_curve.data.splines:
        return sum(spline.calc_length() for spline in evaluated_curve.data.splines)
    
    return 0

# Function to calculate traveled distance
def get_traveled_distance(curve_obj):
    """Calculate the traveled distance based on Evaluation Time."""
    path_anim = curve_obj.data
    eval_time = path_anim.eval_time  # Current evaluation time
    frames = path_anim.path_duration  # Total animation duration in frames
    curve_length = get_curve_length(curve_obj)

    if frames == 0 or curve_length == 0:
        return 0

    return (eval_time / frames) * curve_length

# Function to create a cube (if it doesn't exist)
def create_visualizer_cube():
    """Create a cube that represents traveled distance."""
    cube_name = "Traveled_Distance_Cube"
    if cube_name in bpy.data.objects:
        return bpy.data.objects[cube_name]
    
    bpy.ops.mesh.primitive_cube_add(size=0.2, location=(0, 0, 0))
    cube = bpy.context.object
    cube.name = cube_name
    return cube

# Function to update the cube’s position
def update_visualizer():
    curve = bpy.data.objects.get("track-curve")  # Change to your curve's name
    cube = create_visualizer_cube()  # Get or create the visualizer cube

    if curve and curve.data:
        traveled_distance = get_traveled_distance(curve)

        # Store the traveled distance in curve properties
        if "traveled_distance" not in curve.data:
            curve.data["traveled_distance"] = 0.0
        curve.data["traveled_distance"] = traveled_distance

        # Move the cube along the X-axis
        cube.location.x = traveled_distance

# Update every frame
def frame_change_handler(scene):
    update_visualizer()

# Clear previous handlers and add the new one
bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(frame_change_handler)

# Run once to initialize
update_visualizer()
