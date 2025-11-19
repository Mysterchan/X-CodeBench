import sys

def main():
	data = sys.stdin.read().split()
	t = int(data[0])
	index = 1
	results = []
	for _ in range(t):
		l1 = int(data[index])
		r1 = int(data[index+1])
		l2 = int(data[index+2])
		r2 = int(data[index+3])
		index += 4
		stack = [(l1, r1, l2, r2)]
		count = 0
		while stack:
			x0, x1, y0, y1 = stack.pop()
			if x0 >= x1 or y0 >= y1:
				continue
			w = x1 - x0
			h = y1 - y0
			if w == h and w > 0 and (w & (w - 1)) == 0:
				if x0 % w == 0 and y0 % w == 0:
					count += 1
					continue
			if w == 0 or h == 0:
				count += w * h
				continue
			s_val = 1 << (min(w, h).bit_length() - 1)
			next_x = None
			next_y = None
			next_x_val = (x0 + s_val) // s_val * s_val
			if next_x_val < x1:
				next_x = next_x_val
			next_y_val = (y0 + s_val) // s_val * s_val
			if next_y_val < y1:
				next_y = next_y_val
			if next_x is not None and next_y is not None:
				stack.append((x0, next_x, y0, next_y))
				stack.append((x0, next_x, next_y, y1))
				stack.append((next_x, x1, y0, next_y))
				stack.append((next_x, x1, next_y, y1))
			elif next_x is not None:
				stack.append((x0, next_x, y0, y1))
				stack.append((next_x, x1, y0, y1))
			elif next_y is not None:
				stack.append((x0, x1, y0, next_y))
				stack.append((x0, x1, next_y, y1))
			else:
				count += w * h
		results.append(str(count))
	print("\n".join(results))

if __name__ == "__main__":
	main()
