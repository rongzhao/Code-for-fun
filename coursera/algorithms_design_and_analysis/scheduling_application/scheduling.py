"""Implement greedy algorithm for minimizing sum of weighted completion times given a set of jobs with positive and integral weights and lengths"""


"""Get a set of jobs along with their corresponding weights and lengths from a file"""
def get_jobs(file_name):
	jobs = {}
	with open(file_name, 'r') as f_open:
		job_id = 1
		number_of_jobs = f_open.next()
		for row in f_open:
			row_split = row.rstrip('\n').split()
			weight, length = int(row_split[0]), int(row_split[1])
			jobs[job_id] = [weight, length]
			job_id += 1
	return jobs

"""Calculate a score for each job using its weight and length. The optimal formula is to use ratio"""
def add_score(jobs, score_formula="ratio"):
	if score_formula:
		if score_formula == 'difference':
			for job_id in jobs:
				jobs[job_id].append(jobs[job_id][0] - jobs[job_id][1])
		elif score_formula == 'ratio':
			for job_id in jobs:
				jobs[job_id].append(jobs[job_id][0]/float(jobs[job_id][1]))

"""Compare two jobs' scores"""
def first_is_larger(first_job_id, second_job_id, jobs):
	if jobs[first_job_id][2] > jobs[second_job_id][2]:
		return True
	elif jobs[first_job_id][2] < jobs[second_job_id][2]:
		return False
	else:
		if jobs[first_job_id][0] > jobs[second_job_id][0]:
			return True
		else:
			return False

"""Merge function in merge sort"""
def merge(first_half_ids, second_half_ids, jobs):
	sorted_job_ids = []
	length1, length2 = len(first_half_ids), len(second_half_ids)
	i, j = 0, 0
	while i < length1 and j < length2:
		if first_is_larger(first_half_ids[i], second_half_ids[j], jobs):
			sorted_job_ids.append(first_half_ids[i])
			i += 1
		else:
			sorted_job_ids.append(second_half_ids[j])
			j += 1
	while i < length1:
		sorted_job_ids.append(first_half_ids[i])
		i += 1
	while j < length2:
		sorted_job_ids.append(second_half_ids[j])
		j += 1
	return sorted_job_ids

"""Merge sort"""
def sort(job_ids, jobs):
	length = len(job_ids)
	if length <= 1:
		return job_ids
	first_half, second_half = job_ids[:length/2], job_ids[length/2:]
	first_half_sorted = sort(first_half, jobs)
	second_half_sorted = sort(second_half, jobs)
	sorted_job_ids = merge(first_half_sorted, second_half_sorted, jobs)
	return sorted_job_ids

"""Greedy algorithm to include a job with hightest score in each iteration"""
def greedy_algorithm(jobs):
	job_ids = jobs.keys()
	schedule = sort(job_ids, jobs)
	return schedule

"""Calculate sum of weighted completion times of jobs"""
def get_weighted_sum(schedule, jobs):
	completion_time = 0
	weighted_sum = 0
	for job_id in schedule:
		completion_time += jobs[job_id][1]
		weighted_sum += jobs[job_id][0] * completion_time
	return weighted_sum

"""Main function"""
def main(score_formula='ratio'):
	file_name = "jobs.txt"
	jobs = get_jobs(file_name)
	add_score(jobs, score_formula)
	schedule = greedy_algorithm(jobs)
	sum_weighted_completion_time = get_weighted_sum(schedule, jobs)
	print "Sum of weighted completion time is: ", sum_weighted_completion_time


if __name__ == '__main__':
	main('difference')
	main()
