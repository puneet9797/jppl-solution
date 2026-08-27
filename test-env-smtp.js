const nodemailer = require('nodemailer');
const fs = require('fs');

// Simple parser for .env.local variables
if (fs.existsSync('.env.local')) {
    const env = fs.readFileSync('.env.local', 'utf-8');
    env.split('\n').forEach(line => {
        const parts = line.split('=');
        if (parts.length >= 2) {
            const key = parts[0].trim();
            const val = parts.slice(1).join('=').trim().replace(/^['"]|['"]$/g, '');
            process.env[key] = val;
        }
    });
}

async function main() {
    console.log("Configuring transporter with Vercel Environment Variables...");
    const user = process.env.GMAIL_USER || 'jioliteproducts@gmail.com';
    const pass = process.env.GMAIL_PASS;

    console.log("User email to authenticate:", user);
    console.log("Password retrieved (length):", pass ? pass.length : 'undefined');

    if (!pass) {
        console.error("ERROR: GMAIL_PASS environment variable was not found in .env.local!");
        return;
    }

    const transporter = nodemailer.createTransport({
        host: 'smtp.gmail.com',
        port: 465,
        secure: true,
        auth: {
            user: user,
            pass: pass
        }
    });

    console.log("Verifying connection to SMTP...");
    try {
        await transporter.verify();
        console.log("SUCCESS: Connection to Gmail SMTP server is verified and authentic!");

        console.log("Sending a verification email...");
        const info = await transporter.sendMail({
            from: `"JPPL Verification" <${user}>`,
            to: user,
            subject: 'JPPL SMTP Pipeline Verification - SUCCESS',
            html: `
                <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #d4af37; border-radius: 8px; background-color: #f8fafc;">
                    <h2 style="color: #0F2942; border-bottom: 2px solid #D4AF37; padding-bottom: 10px;">SMTP Connection Verified</h2>
                    <p style="font-size: 16px; color: #1e293b;">This email confirms that the nodemailer SMTP configuration for JPPL Digital Services is successfully configured and authenticated with the Gmail App Password from Vercel env.</p>
                    <p style="font-size: 14px; color: #64748b;">Timestamp: ${new Date().toISOString()}</p>
                </div>
            `
        });
        console.log("SUCCESS: Test email sent! Message ID:", info.messageId);
    } catch (error) {
        console.error("ERROR: SMTP connection failed:", error);
    }
}

main();
