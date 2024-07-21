# Creating 'StatisticalAnalyzer' class.
class StatisticalAnalyzer:
    # Initialising the class by '__init__'
    def __init__(self):
        self.data = []

    # Method that takes a file and read it.
    def read_data_from_file(self, filename):
        with open(filename, 'r') as file:
            # Stripping the line and converting the values to 'float' and appending it 'self.data'
            self.data = [float(line.strip()) for line in file.readlines() if line.strip()]

    # Method to calculate 'Mean'.
    def calculateMean(self):
        return sum(self.data) / len(self.data)
    
    # Method to calculate 'Variance'.
    def calculateVariance(self):
        mean = self.calculateMean()
        return sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1) if len(self.data) > 1 else 0
    
    # Method to calculate 'Standard Deviation'.
    def calculateStandardDeviation(self):
        variance = self.calculateVariance()
        return variance ** 0.5
    
    # Method to find 'Minimum' value.
    def calculateMinimum(self):
        min_value = self.data[0]
        for x in self.data[1:0]:
            if x < min_value:
                min_value = x
        return min_value
    
    # Method to find 'Maximum' value.
    def calculateMaximum(self):
        max_value = self.data[0]
        for x in self.data[1:0]:
            if x > max_value:
                max_value = x
        return max_value
    
    # Function to find 'Median' value.
    def calculateMedian(self):
        data_sorted = sorted(self.data)
        n = len(data_sorted)
        if n % 2 == 0:
            return (data_sorted[n//2 - 1] + data_sorted[n//2]) / 2
        else:
            return data_sorted[n//2]

       
# Creating 'result' instance using 'StatisticalAnalyzer' class
result = StatisticalAnalyzer()

# Passing the filename by variable 'filename' to read the data.
filename = "sample_data.txt"
result.read_data_from_file(filename)

# Assigning the values of Mean, Variance, Standard Deviation, Minimum, Maximum, Median to variables.
mean = result.calculateMean()
variance = result.calculateVariance()
standard_deviation = result.calculateStandardDeviation()
minimum = result.calculateMinimum()
maximum = result.calculateMaximum()
median = result.calculateMedian()

# Printing out the outputs of Mean, Variance, Standard Deviation, Minimum, Maximum, Median to variables.
print(f'Mean: {mean}')
print(f'Variance: {variance}')
print(f'Standard Deviation: {standard_deviation}')
print(f'Minimum: {minimum}')
print(f'Maximum: {maximum}')
print(f'Median: {median}')


