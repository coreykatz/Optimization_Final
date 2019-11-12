# Optimization Final
This is my portion of a final project for an Optimization course taken in Fall 2018. This purpose of this project was to approximate probability density functions of unknown distributions. I focused on interpolation and polynomial regression on histograms. The .py file contains my functions to implement my methods and the second file is my portion of the report.  


\textbf{Normal($\mu = 3$, $\sigma ^ 2 = 4$):}

$$f(x;3,4)=\frac{1}{\sqrt{8\pi
}}e^{-\frac{(x-3)^2}{8}}$$

\textbf{Bimodal: $\frac{1}{2}$(Normal($\mu = -2$, $\sigma ^ 2 = 1$) + Normal($\mu = 2$, $\sigma ^ 2 = 2$):}
$$f(x)=\frac{1}{2}(\frac{1}{\sqrt{2\pi
}}e^{-\frac{(x+2)^2}{1}}+\frac{1}{\sqrt{8\pi
}}e^{-\frac{(x-2)^2}{8}})$$

\newline


\textbf{Exponentially Modified Normal with $\lambda=0.1$, $\mu = 0$ and $\sigma=2$: }

$$f(x; \mu, \sigma, \lambda)=\frac{\lambda}{2}e ^ {\frac{\lambda}{2}(2\mu + \lambda\sigma ^ 2 - 2x)} \textit{erfc}\Big(\frac{\mu + \lambda\sigma ^ 2 - x}{\sqrt{2}\sigma}\Big) = 0.05 e ^ {0.02 - 0.1x} \textit{erfc} (\frac{0.4 - x}{2\sqrt{2}})$$

\begin{center}
    where $\textit{erfc}$ is the complementary error function defined as \newline
    
    $\textit{erfc}(x) = 1 - \textit{erf}(x) = \frac{2}{\sqrt{\pi}}\int_x^\infty e^{-t^2}dt$
\end{center}
