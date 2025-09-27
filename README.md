# White Label ATM Locator & Management System

A specialized tool for managing and locating independent, non-bank ATMs (White Label ATMs). Essential for financial access in remote, underserved, and disaster-prone areas.

## 🚀 Purpose & Why It's Needed

This system addresses a critical gap in financial infrastructure. Traditional bank ATMs are often concentrated in urban centers. This repository helps manage the network of White Label ATMs, which are crucial for:
*   **Financial Inclusion:** Providing ATM services in rural and remote locations where banks don't have branches.
*   **Disaster Resilience (e.g., Floods):** When floods damage bank branches and their ATMs, White Label ATMs (often located in sturdy, elevated retail locations) can be the only remaining source of cash for emergency supplies, medicine, and recovery. This system helps people find operational ATMs during a crisis.
*   **Operational Management:** Allows operators to manage ATM data, fees, and status efficiently.

## 📁 How to Open the Project

### Prerequisites
*   **Node.js** (v16 or higher) installed on your machine.
*   **Git** for version control.
*   A code editor like VS Code.

### Steps
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/white-label-atm-repo.git
    ```
2.  **Navigate to the Project Directory:**
    ```bash
    cd white-label-atm-repo
    ```
3.  **Install Dependencies:**
    ```bash
    npm install
    ```
4.  **Start the Development Server:**
    ```bash
    npm start
    ```
5.  **Open your browser** and go to `http://localhost:3000`.

## 💾 How to Save Your Work

This project uses Git for version control. To save your changes:

1.  **Stage the files you've changed:**
    ```bash
    git add .
    ```
2.  **Commit the changes with a descriptive message:**
    ```bash
    git commit -m "Added new ATM location data for flood-prone region X"
    ```
3.  **Push the changes to the remote repository (like GitHub):**
    ```bash
    git push origin main
    ```

## 🆘 How It Helps in a Flood Scenario

During a flood, this system becomes a vital public utility:

1.  **Real-Time Status Check:** API integrations show which ATMs are still operational, have power, and are stocked with cash.
2.  **Location-Based Search:** Citizens and aid workers can find the nearest functioning ATM on a map, filtering out ones in flooded zones.
3.  **Critical Information:** Displays surcharge fees and operating hours, helping people plan their trips efficiently during an emergency.
4.  **Data for Aid Agencies:** Provides crucial data to government and relief organizations about where financial access points are still available, informing disaster response efforts.

### Example Use Case:
> *"A flood has submerged the downtown core, disabling all bank branches. A resident uses this app to find a White Label ATM inside a gas station on higher ground that is still operational, allowing them to withdraw cash for essential supplies."*
