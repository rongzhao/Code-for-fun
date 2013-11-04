import numpy as np

class matrix_factorization:
    def __init__(self, R, Theta, X, K, alpha = 0.0001, beta = 0.1):
        self.steps = 5000
        self.step = 0
        self.alpha = alpha #learning rate
        self.beta = beta   #lambda
        self.is_converge = False

        self.rating_matrix = R
        self.Theta = Theta #user matrix
        self.X = X.T       #business matrix
        self.K = K         #number of features
        self.new_Theta = Theta
        self.new_X = X.T

        self.current_error = 0
      
    def training(self):
        self.current_error = self.cost_function("old")
        while((not self.is_converge) and (self.step <= self.steps)):
            current_cost = self.current_error
            if current_cost < 0.1:
                self.is_converge = True
                print "current error is smaller than 0.1"
                break
            if self.alpha < 1e-10:
                self.is_converge = True
                print "learning rate is smaller than 1e-10"
                break
            print "current sum of error =", current_cost
            print "The learning rate =", self.alpha
            print "step", self.step
            self.try_update()
            new_cost = self.cost_function("new")
            if new_cost < current_cost:
                self.apply_update()
                self.alpha *= 1.25
                self.current_error = new_cost
                self.step += 1
                if current_cost - new_cost < 0.05:
                    self.is_converge = True
                    print "error difference is smaller than 0.05"
                    break
            else:
                self.alpha *= 0.5               
        return self.Theta, self.X.T

    def cost_function(self, indicator):
        if indicator == "old":
            user = self.Theta
            business = self.X
        else:
            user = self.new_Theta
            business = self.new_X
        e = 0
        for record in self.rating_matrix:
            i, j, rating = record[1], record[0], record[2]
            e = e + pow((rating - np.dot(user[i,:], business[:,j])), 2)
        for k in xrange(self.K):
            for i in xrange(len(user)):
                e = e + self.beta * (pow(user[i][k], 2))
            for j in xrange(len(business[0])):
                e = e + self.beta * (pow(business[k][j], 2))
        return e
        
    def try_update(self):
        for record in self.rating_matrix: 
            i, j, rating = record[1], record[0], record[2]
            eij = rating - np.dot(self.Theta[i,:], self.X[:,j])
            for k in xrange(self.K):
                self.new_Theta[i,k] = self.Theta[i,k] + self.alpha * (2 * eij * self.X[k,j] - self.beta * self.Theta[i,k])
                self.new_X[k,j] = self.X[k,j] + self.alpha * (2 * eij * self.Theta[i, k] - self.beta * self.X[k, j])

    def apply_update(self): 
        for i in xrange(len(self.Theta)):
            for k in xrange(self.K):
                self.Theta[i, k] = self.new_Theta[i, k]
        for j in xrange(len(self.X[0])):
            for k in xrange(self.K):
                self.X[k, j] = self.new_X[k, j]


            
