from p5 import *
from slider import *

angle_slider = Slider(0, TWO_PI, PI / 4)
color = 0

def setup():
	title('Brócolis fractal')
	size(400, 400)
	angle_slider.position(20, 20)

def draw():
	angle = angle_slider.value()
	tree_level = 0
	color = 0
	weight = 5
	
	background(50)
	stroke(255)
	translate(200, height)
	
	branch(120, tree_level, color, angle, weight)

def branch(length, tree_level, color, angle, weight):
	stroke(color, 255, color)
	stroke_weight(weight)
	line((0, 0), (0, -length))
	translate(0, -length) 

	color = mapping(tree_level, 0, 9, 255, 0)
	if length > 4:
		angle -= 0.08
		tree_level += 1
		weight *= 0.6
		with push_matrix(): # galho esquerdo
			rotate(angle)
			branch(length * 0.67, tree_level, color, angle, weight)
		with push_matrix(): # galho direito
			rotate(-angle)
			branch(length * 0.67, tree_level, color, angle, weight)
			
if __name__ == '__main__':
	run()