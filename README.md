# HiveMind
An exploration into the publicly available EEGLAB discussion forum annual archives provided by the Swartz Center at UCSD, which can be found at:
https://sccn.ucsd.edu/pipermail/eeglablist/

This is a fun, personal project to indulge in using AWK and Python, extracting data and visualizing it in a geospatial and temporal format.  As a long time user of EEGLAB and data scientist (mainly outside of work, but also at work when they let me), this seemed an interesting and worthwhile investigation - not just for myself, but also potentially those in the EEG world to see the arc of one of the field's most utilized tools.  

Institutional messaging is tracked over time and documented via Longitudinal and Latitudinal coordinates on a world map. This abstracts the information of each poster for privacy reasons.  (The posters' information is available in the forum archives should one dig themselves, but I do not reveal more information than necessary.)  Similarly, regarding institutional messages catalogued, I only include those with verified institutional addresses.  All personal gmail, yahoo, spymac, etc. addresses are discarded when plotting locations due to privacy matters and to avoid having to identify institutions manually. (I only have so much time on this rock.)

Textual Analysis may also be performed to track discussion point, birthpoints, and popularization of some of the most impactful libraries and toolkits used in EEG analysis.

Technologies Used:
- GNU Awk 5.1.0, API: 3.0
- Python 3.10.12
- Python Virtual Environment Packages can be found in the requirements.txt file in the root of this repository.
- My Brain, which as you will see in the resulting images and plots is an individual-based tool common amongst all us brain fanatics that we love to think and talk about tirelessly.

As this project progresses, visualizations will be enhanced and improved.  Since cleaning and extraction has finally been settled and begun, here is the global map of all neuroscience discussion in the EEGLAB forums maintained by UCSD in the years 2004-2024.

<h3 align="center">All EEGLAB Forum Communications (2004-2024):</h3>

<p align="center">
    <img width="640" height="480" src="https://github.com/culliokw/HiveMind/blob/main/Maps/communication.gif" alt="Communications Map">
</p>
