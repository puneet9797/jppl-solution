// Helper to log lead data to Google Sheets via Google Apps Script Web App
async function logToGoogleSheets(data) {
    const scriptUrl = process.env.GOOGLE_SCRIPT_URL;
    if (!scriptUrl) {
        console.warn('Google Sheets logging skipped: GOOGLE_SCRIPT_URL environment variable is not defined.');
        return false;
    }

    try {
        const selectedServices = data.formType === 'quick'
            ? (data.service || 'General Consultation')
            : (Array.isArray(data.services) && data.services.length > 0 ? data.services.join(', ') : 'General Inquiry / Consultation');

        const payload = {
            formType: data.formType,
            name: data.name,
            phone: data.phone,
            email: data.email || 'N/A',
            location: data.location || 'N/A',
            selectedServices: selectedServices,
            message: data.message || data.comments || 'N/A'
        };

        const response = await fetch(scriptUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Google Sheets response:', result);
        return result.success;
    } catch (error) {
        console.error('Error logging to Google Sheets:', error);
        return false;
    }
}

module.exports = async (req, res) => {
    // Enable CORS for frontend requests
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
    res.setHeader(
        'Access-Control-Allow-Headers',
        'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
    );

    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }

    if (req.method !== 'POST') {
        res.status(405).json({ success: false, message: 'Method Not Allowed' });
        return;
    }

    try {
        const { name, phone } = req.body;

        // Validation
        if (!name || !phone) {
            res.status(400).json({ success: false, message: 'Missing required parameters: name, phone' });
            return;
        }

        // Log to Google Sheets
        const sheetsSuccess = await logToGoogleSheets(req.body);
        
        if (sheetsSuccess) {
            res.status(200).json({ success: true, message: 'Inquiry successfully saved!' });
        } else {
            res.status(500).json({ success: false, message: 'Failed to record inquiry in lead database' });
        }

    } catch (error) {
        console.error('Error handling inquiry request:', error);
        res.status(500).json({ success: false, message: 'Server error handling inquiry', error: error.message });
    }
};
