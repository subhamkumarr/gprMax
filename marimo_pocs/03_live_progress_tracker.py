import marimo

__generated_with = "0.2.1"

app = marimo.App(width="medium")

@app.cell
def __(mo):
    title = mo.md(
        """
        # gprMax Reactive Progress Tracker POC

        This POC demonstrates how `marimo` can asynchronously track long-running `gprMax` simulations. 
        Instead of waiting for a black terminal window to finish, the browser natively displays 
        a beautiful progress bar that accurately reflects the iteration count!
        
        *Hit the "Execute gprMax Simulation" switch below to see the progress hook activate.*
        """
    )
    return title,

@app.cell
def __(mo):
    run_toggle = mo.ui.switch(label="🚀 Execute gprMax Simulation")
    
    ui_container = mo.vstack([
        mo.md("### Simulation Controls"),
        run_toggle
    ])
    ui_container
    return run_toggle, ui_container

@app.cell
def __(run_toggle, mo, time):
    if not run_toggle.value:
        output_ui = mo.md("**Status:** ⏸️ Idle. Waiting to execute `.in` file...")
    else:
        # Simulate a gprMax C/CUDA loop taking time
        for i in mo.status.progress_bar(
            range(100), 
            title="Executing gprMax FDTD Solver 🚀", 
            subtitle="Calculating Electromagnetic Fields... (Iteration parsing hook)"
        ):
            time.sleep(0.05) # Simulate execution time
            
        output_ui = mo.md(
            f"✅ **Simulation Complete!** \n\n"
            f"Output successfully written to `simulation_bscan.out`. You can now analyze it."
        )
    output_ui
    return output_ui,

@app.cell
def __():
    import marimo as mo
    import time
    return mo, time

if __name__ == "__main__":
    app.run()
