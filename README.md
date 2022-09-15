# Energy Communities Web Application


<header>
<p>This Web Application is created using python as a languange with Streamlit, numpy, pandas, and mapbox as the libraries. This energy community calculation is comprises of energy calculation, economical calculation, and energy classification. The application has four pages these are Home, Calculation, Result, and Contact. The main feature is particularly in Calculation page. There are six phases with four possible result in the algorithm. These are decided whether the user will consider a storage and input their solar PV capacity.</p>
</br>
<p>Here is how you can use Web Application:</p>
<ol>
<li>Open the calculation site</li>
<li>Select the Longitude and Latitude by searching your address and click the point that you pick</li>
<li>Insert the Longitude and Latitude from the box result in the map section into the form</li>
<li>Pick your country that you live, this is deciding the rate of the electricity</li>
<li>Select the stage of your project</li>
<li>Select the types of the energy community</li>
<li>Choose if you want to consider a storage that connects with the solar PV</li>
<li>Pick if you want to introduce the capacity</li>
<ul>
<li>If you pick introduced, input your solar capacity</li>
<li>If you pick Recommeneded, you neeed to fill up the estimation area and the quantity of the building</li>
</ul>
<li>Finally, decide which type of energy communities and input the amount</li>
<li>Define each value of the energy community</li>
<li>Click (Submit) button</li>
<li>The result is placed in Result Page which divided into three section based on the energy calculation, economical calculation, and energy classification</li>
</ol>
</header>

<nav>
<h3>There are prerequisite package modules that you need to install</h3>
<p>This is how you can download it, open the command line (terminal) in your windows or IDE. Type this pip if you have already install it. However you can as well replace "pip" with "pyhton -m pip".</p>
<ul>
<li>pip install streamlit</li>
<li>pip install jsonlib</li>
<li>pip install Pillow</li>
<li>pip install pandas</li>
<li>pip install matplotlib</li>
<li>pip install numpy</li>
</ul>

   <h3>How to run locally</h3>
<p>After installing the the libraries as a package module, you need to know that there are two outsource library it is provided by MAPBOX and RENEWABLE NINJA. Both API require a token with limits each day 50 request per day for renewable energy and it is unlimited for MAPBOX. To run locally you need to open the terminal and type <span><b>"streamlit run app.py"</b></span> however incase you cannot add the streamlit to your path you can also use <span><b>"python -m streamlit run app.py"</b></span></p>

 <h3>Limitiation</h3>
<p>Streamlit is a library that is very limited for developing a web application, it is for merely data visualization. These are the limitation of the web application whether it is caused by the limitation of Streamlit or even by the features provided.</p>
<ul>
<li>There is no routing system</li>
<li>Not eligible for multiple step forms</li>
<li>Not able to send parameters to the URL from JS to Python</li>
<li>There is no required attributes in input forms</li>
<li>Button cannot be hyperlink to other pages</li>
<li>Changing interface is not flexible</li>
<li>Only one streamlit form can be created in a page because when the forms is submitted it triggers the whole page to be reloaded</li>
<li>To pass variable between pages only limited using session because there is no routing hence the variable cannot just be exported and imported between pages.</li>
<li>Not every variable is passed from the calculation page to result page since not every information is needed in the result page</li>
</ul>

<p>The web apps still requires enchancement and refinement, feel free to fetch the code from the github</p>

<p>In this web application, we also apply some assumption to the calculation. These are as listed below:</p>
<ul>
<li>To calculate the energy storage we decide the battery sizing is 60% of the RES capacity value </li>
<li>We recommend the RES capacity based on the area and the effective value is 80%. Moreover, each solar PV has 0.5 KWP capacity</li>
<li>If there is no storage sizing we consider the energy saving is only 70% of the RES potential</li>
<li>The price rate of the electricity is 250 euros/MWh, it applies the same for all of the 10 countries. </li>
</ul>
</nav>

<footer>
<b>This is copyrighted by R2M Solution</b>
</footer>

