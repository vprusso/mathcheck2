rowswaps = [[4,1,7,6,0,5,3,2,55,54,52,36,53,51,27,18,50,61,15,48,42,77,70,34,24,66,60,14,47,79,74,41,76,69,23,58,11,75,72,39,67,31,20,63,62,59,57,28,19,56,16,13,10,12,9,8,49,46,35,45,26,17,44,43,78,71,25,40,68,33,22,65,38,73,30,37,32,21,64,29],
[1,4,6,7,5,0,3,2,36,53,51,55,54,52,27,50,18,61,60,58,62,59,57,28,56,19,15,14,11,12,9,16,13,10,8,48,47,35,45,49,46,26,44,17,42,77,70,34,66,24,41,76,69,79,74,23,39,67,75,72,31,63,20,43,40,38,37,78,73,32,64,21,71,68,29,25,33,65,22,30],
[6,2,1,5,7,3,0,4,45,9,51,71,29,69,68,70,67,56,57,19,62,28,60,59,61,58,64,73,21,12,53,78,32,76,77,37,38,35,36,43,41,40,42,39,44,8,50,65,66,63,46,10,52,30,74,72,17,18,25,23,22,24,20,49,26,47,48,16,14,13,15,11,55,27,54,75,33,34,31,79],
[3,7,1,5,2,6,4,0,59,54,13,65,79,33,68,22,40,49,46,48,44,47,26,45,17,35,78,73,77,53,12,64,76,32,21,75,72,58,11,63,31,67,20,39,62,55,16,71,25,43,57,52,10,74,30,38,61,15,66,34,70,24,42,56,60,28,19,50,27,51,18,36,8,14,9,37,69,23,41,29],
[7,3,5,1,6,2,4,0,65,79,33,59,54,13,68,40,22,49,78,75,62,55,16,71,43,25,46,73,72,74,30,57,52,10,38,48,77,66,34,61,15,70,42,24,44,47,26,45,35,17,64,76,32,53,12,21,63,31,58,11,67,39,20,56,50,8,37,60,14,69,41,23,28,27,29,19,51,36,18,9],
[5,0,7,6,1,4,2,3,34,30,33,28,29,32,27,26,31,43,16,25,62,71,78,55,49,75,41,14,23,74,79,60,69,76,47,37,8,66,65,56,64,50,44,63,42,38,40,36,35,39,15,10,13,9,12,11,24,22,19,21,18,17,20,61,70,77,48,57,73,52,46,72,59,68,54,58,51,45,67,53],
[2,6,5,1,3,7,0,4,71,29,69,45,9,51,68,67,70,56,64,37,44,8,50,65,63,66,57,73,38,30,74,46,10,52,72,19,21,25,23,17,18,22,20,24,62,28,60,59,58,61,78,32,76,12,53,77,43,41,35,36,40,39,42,49,16,55,75,26,27,33,31,34,47,14,79,48,13,11,15,54],
[1,0,3,2,5,4,6,7,11,12,13,8,9,10,14,16,15,17,26,35,44,45,46,47,49,48,18,27,36,53,54,50,51,52,55,19,28,58,59,56,57,60,62,61,20,21,22,23,25,24,31,32,33,29,30,34,39,40,37,38,41,43,42,63,67,72,75,64,73,76,78,77,65,68,79,66,69,71,70,74],
[0,5,6,7,4,1,2,3,28,29,32,34,30,33,27,31,26,43,41,37,42,38,40,36,39,35,16,14,8,9,12,15,10,13,11,25,23,19,21,24,22,18,20,17,62,71,78,55,75,49,60,69,76,74,79,47,56,64,66,65,50,63,44,61,57,59,58,70,68,51,67,45,77,73,53,48,52,72,46,54],
[5,4,2,3,1,0,7,6,23,74,69,47,79,76,14,60,41,63,50,66,44,65,64,8,56,37,31,27,34,30,29,26,33,32,28,75,55,25,71,49,78,16,62,43,20,72,67,11,58,39,18,52,51,54,53,36,24,70,48,77,15,61,42,17,22,21,19,46,73,10,57,38,45,68,9,35,13,59,40,12],
[4,5,3,2,0,1,7,6,47,79,76,23,74,69,14,41,60,63,31,75,20,72,67,11,39,58,50,27,55,54,53,18,52,51,36,66,34,48,77,24,70,15,42,61,44,65,64,8,37,56,26,33,32,30,29,28,49,78,25,71,16,43,62,17,46,45,35,22,68,13,40,59,21,73,12,19,10,38,57,9],
[6,3,0,4,7,2,1,5,21,12,32,77,53,76,73,78,64,39,40,35,42,36,41,38,43,37,67,68,45,9,29,70,51,69,71,58,59,19,28,61,60,57,62,56,20,11,31,72,75,63,22,13,33,54,79,65,17,26,48,47,46,49,44,24,18,23,25,15,14,10,16,8,34,27,30,66,52,55,50,74],
[3,6,4,0,2,7,1,5,77,53,76,21,12,32,73,64,78,39,67,58,20,11,31,72,63,75,40,68,59,54,79,22,13,33,65,35,45,48,47,17,26,46,44,49,42,36,41,38,37,43,70,51,69,9,29,71,61,60,19,28,57,56,62,24,15,34,66,18,27,52,50,55,23,14,74,25,10,8,16,30],
[2,7,0,4,3,6,5,1,38,30,10,72,74,52,73,46,57,24,22,25,20,23,18,21,17,19,70,68,71,29,9,67,69,51,45,66,65,37,8,63,50,64,44,56,42,34,15,77,48,61,40,33,13,79,54,59,43,16,75,55,78,49,62,39,41,36,35,31,27,32,26,28,11,14,12,58,76,47,60,53],
[7,2,4,0,6,3,5,1,72,74,52,38,30,10,73,57,46,24,70,66,42,34,15,77,61,48,22,68,65,79,54,40,33,13,59,25,71,75,55,43,16,78,62,49,20,23,18,21,19,17,67,69,51,29,9,45,63,50,37,8,64,56,44,39,31,11,58,41,14,76,60,47,36,27,53,35,32,28,26,12],
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79]]
colswaps = [[5,14,13,10,6,0,4,15,12,9,3,11,8,2,1,7,25,17,23,21,20,19,27,18,26,16,24,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[5,6,0,4,14,13,10,3,11,8,15,12,9,2,7,1,21,20,19,25,17,23,27,26,18,24,16,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[8,6,11,3,7,9,1,4,0,5,15,2,13,12,14,10,26,27,25,19,22,23,20,21,24,18,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[12,4,11,10,15,9,14,6,5,0,7,13,2,8,1,3,24,22,16,21,27,18,20,19,26,23,25,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[12,15,9,14,4,11,10,7,13,2,6,5,0,8,3,1,21,27,18,24,22,16,20,26,19,25,23,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[2,15,13,7,3,0,1,14,9,12,6,8,11,5,4,10,26,20,24,18,17,16,27,21,25,19,23,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[8,7,9,1,6,11,3,15,2,13,4,0,5,12,10,14,19,22,23,26,27,25,20,24,21,16,18,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[0,4,5,6,1,2,3,10,11,12,7,8,9,13,15,14,19,20,21,16,17,18,22,24,23,26,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[2,3,0,1,15,13,7,6,8,11,14,9,12,5,10,4,18,17,16,26,20,24,27,25,21,23,19,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[13,7,2,15,10,5,14,1,9,8,4,12,11,0,6,3,24,20,26,23,17,25,22,19,16,21,18,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[13,10,5,14,7,2,15,4,12,11,1,9,8,0,3,6,23,17,25,24,20,26,22,16,19,18,21,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[11,3,8,6,10,12,4,1,0,2,14,5,13,9,15,7,25,27,26,16,22,24,17,18,23,21,19,20,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[11,10,12,4,3,8,6,14,5,13,1,0,2,9,7,15,16,22,24,25,27,26,17,23,18,19,21,20,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[9,1,8,7,14,12,15,3,2,0,10,13,5,11,4,6,23,22,19,18,27,21,17,16,25,24,26,20,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[9,14,12,15,1,8,7,10,13,5,3,2,0,11,6,4,18,27,21,23,22,19,17,25,16,26,24,20,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59],
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]]
identity_index = 15
order = 16
ncols = 60
