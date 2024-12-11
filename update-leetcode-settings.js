const fs = require('fs');
const path = require('path');

// 获取当前日期并格式化
const now = new Date();
const year = now.getFullYear();
const month = String(now.getMonth() + 1).padStart(2, '0');
const day = String(now.getDate()).padStart(2, '0');
const dateStr = `${year}-${month}-${day}`;

// 设置文件路径
const settingsPath = path.join(process.env.APPDATA, 'Cursor', 'User', 'settings.json');

// 读取现有的 settings.json
fs.readFile(settingsPath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading settings file:', err);
        return;
    }

    // 解析现有设置
    const settings = JSON.parse(data);
    
    // 更新 leetcode.workspaceFolder
    settings['leetcode.workspaceFolder'] = `C:\\Users\\huang\\Documents\\vscode_hsh\\leetcode_hsh\\${dateStr}`;

    // 写回文件
    fs.writeFile(settingsPath, JSON.stringify(settings, null, 4), (err) => {
        if (err) {
            console.error('Error writing settings file:', err);
            return;
        }
        console.log('Settings updated successfully');
    });
}); 