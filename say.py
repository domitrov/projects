import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DesmosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desmos-like Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Entry for user input
        self.expression_entry = ttk.Entry(self.root, width=50)
        self.expression_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Button to plot the graph
        plot_button = ttk.Button(self.root, text="Plot", command=self.plot_graph)
        plot_button.grid(row=0, column=2, padx=10, pady=10)

        # Matplotlib figure
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot_area = self.figure.add_subplot(111)

        # Canvas for embedding Matplotlib figure in Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)

    def plot_graph(self):
        expression = self.expression_entry.get()

        try:
            x = range(-10, 11)
            y = [eval(expression) for i in x]

            # Clear previous plot
            self.plot_area.clear()

            # Plot the new graph
            self.plot_area.plot(x, y)
            self.plot_area.set_title("Graph of " + expression)
            self.plot_area.set_xlabel("x-axis")
            self.plot_area.set_ylabel("y-axis")

            # Redraw canvas
            self.canvas.draw()

        except Exception as e:
            print(f"Error: {e}")
            # You might want to handle errors more gracefully

if __name__ == "__main__":
    root = tk.Tk()
    app = DesmosApp(root)
    root.mainloop()
