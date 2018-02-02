"""change this class to a line class"""
  """def poly(self,degree,col,label):
      """Finds the polynomial line of best fit for your GeomList and plots it in colour 'col'.

      Parameters
      ----------
      col : str
          the colour that your polynomial will be plotted
      """
      xs = list()
      ys = list()
      for i in self:
          xs.append(i.x)
          ys.append(i.y)
      z = np.polyfit(xs, ys, deg=degree, rcond=None, full=False, w=None, cov=False)
      p = np.poly1d(z)
      plt.plot(xs, p(xs),'--', linewidth=2, color=col, label=label)"""
