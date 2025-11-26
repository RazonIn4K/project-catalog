import { useState, useEffect } from 'react';
import axios from 'axios';
import { Activity, Play, Pause, Send, Users, CheckCircle, XCircle, AlertTriangle } from 'lucide-react';
import clsx from 'clsx';

// --- Configuration ---
const SIMULATOR_API = "http://localhost:8001";

function App() {
  const [pipelineStats, setPipelineStats] = useState({
    new: 0,
    contacted: 0,
    won: 0,
    lost: 0
  });
  
  const [logs, setLogs] = useState([]);
  const [nurtureActive, setNurtureActive] = useState(true);
  const [loading, setLoading] = useState(false);
  const [systemStatus, setSystemStatus] = useState("offline"); // offline, online

  // --- Polling Logic ---
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch Stats
        const statsRes = await axios.get(`${SIMULATOR_API}/stats`);
        setPipelineStats(statsRes.data);
        
        // Fetch Logs
        const logsRes = await axios.get(`${SIMULATOR_API}/logs`);
        setLogs(logsRes.data);
        
        // Fetch Toggle Status (Initial sync)
        if (systemStatus === "offline") {
            const toggleRes = await axios.get(`${SIMULATOR_API}/control/nurture`);
            setNurtureActive(toggleRes.data.active);
        }

        setSystemStatus("online");
      } catch (err) {
        setSystemStatus("offline");
      }
    };

    // Poll every 2 seconds
    const interval = setInterval(fetchData, 2000);
    fetchData(); // Initial call

    return () => clearInterval(interval);
  }, [systemStatus]);

  // --- Actions ---
  const sendTestLead = async () => {
    setLoading(true);
    try {
      await axios.post(`${SIMULATOR_API}/simulate/ghl/contact-create`, {
        contact_name: `Lead ${Math.floor(Math.random() * 1000)}`
      });
      // Logs will update on next poll
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const toggleNurture = async () => {
    try {
      const newState = !nurtureActive;
      await axios.post(`${SIMULATOR_API}/control/nurture`, { active: newState });
      setNurtureActive(newState);
    } catch (err) {
      console.error("Failed to toggle nurture", err);
    }
  };

  return (
    <div className="min-h-screen p-8 max-w-6xl mx-auto">
      <header className="mb-8 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">HighEncode Studio</h1>
          <p className="text-gray-500">GHL Sandbox Control Plane</p>
        </div>
        <div className={clsx(
            "flex items-center gap-2 text-sm px-3 py-1 rounded-full transition-colors",
            systemStatus === "online" ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"
        )}>
          <span className={clsx(
              "w-2 h-2 rounded-full",
              systemStatus === "online" ? "bg-green-500 animate-pulse" : "bg-red-500"
          )}></span>
          {systemStatus === "online" ? "System Online" : "Jules Offline"}
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        {/* --- Pipeline Summary --- */}
        <div className="md:col-span-3 grid grid-cols-1 sm:grid-cols-4 gap-4">
          <StatCard 
            title="New Leads" 
            value={pipelineStats.new} 
            icon={<Users className="text-blue-500" />} 
            color="bg-blue-50 border-blue-100"
          />
          <StatCard 
            title="Contacted" 
            value={pipelineStats.contacted} 
            icon={<Activity className="text-purple-500" />} 
            color="bg-purple-50 border-purple-100"
          />
          <StatCard 
            title="Won Deals" 
            value={pipelineStats.won} 
            icon={<CheckCircle className="text-green-500" />} 
            color="bg-green-50 border-green-100"
          />
           <StatCard 
            title="Lost" 
            value={pipelineStats.lost} 
            icon={<XCircle className="text-red-500" />} 
            color="bg-red-50 border-red-100"
          />
        </div>

        {/* --- Controls --- */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Activity size={20} /> Controls
          </h2>
          
          <div className="space-y-4">
            <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div>
                <p className="font-medium">Nurture Sequence</p>
                <p className="text-xs text-gray-500">{nurtureActive ? "Active (Auto-Advance)" : "Paused"}</p>
              </div>
              <button 
                onClick={toggleNurture}
                disabled={systemStatus === "offline"}
                className={clsx(
                  "p-2 rounded-full transition-colors disabled:opacity-50",
                  nurtureActive ? "bg-green-100 text-green-600" : "bg-yellow-100 text-yellow-600"
                )}
              >
                {nurtureActive ? <Pause size={18} /> : <Play size={18} />}
              </button>
            </div>

            <div className="border-t pt-4">
              <p className="text-sm text-gray-500 mb-2">Simulation</p>
              <button 
                onClick={sendTestLead}
                disabled={loading || systemStatus === "offline"}
                className="w-full flex items-center justify-center gap-2 bg-black text-white py-2 rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50"
              >
                <Send size={16} />
                {loading ? "Injecting..." : "Send Test Lead"}
              </button>
            </div>
          </div>
        </div>

        {/* --- Automation Log --- */}
        <div className="md:col-span-2 bg-white p-6 rounded-xl shadow-sm border border-gray-200 h-96 overflow-y-auto">
          <h2 className="text-lg font-semibold mb-4 sticky top-0 bg-white pb-2 border-b">Live Automation Log</h2>
          <div className="space-y-3">
            {logs.length === 0 && (
                <p className="text-gray-400 text-center py-8">No events yet. Send a lead!</p>
            )}
            {logs.map((log) => (
              <div key={log.id} className="flex items-center justify-between p-3 border rounded-lg hover:bg-gray-50 transition-colors">
                <div className="flex items-center gap-3">
                  {log.status === 'success' && <CheckCircle size={18} className="text-green-500" />}
                  {log.status === 'warning' && <AlertTriangle size={18} className="text-yellow-500" />}
                  {log.status === 'info' && <Activity size={18} className="text-blue-500" />}
                  {log.status === 'error' && <XCircle size={18} className="text-red-500" />}
                  
                  <span className="font-medium text-sm">{log.event}</span>
                </div>
                <span className="text-xs text-gray-400 font-mono">{log.time}</span>
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
}

function StatCard({ title, value, icon, color }) {
  return (
    <div className={clsx("p-6 rounded-xl border flex items-center justify-between", color)}>
      <div>
        <p className="text-sm text-gray-500 font-medium">{title}</p>
        <p className="text-3xl font-bold mt-1">{value}</p>
      </div>
      <div className="p-3 bg-white rounded-lg shadow-sm">
        {icon}
      </div>
    </div>
  );
}

export default App;
