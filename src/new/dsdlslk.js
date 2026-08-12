const express = require('express')
const mysql = require('mysql2/promise')
const { exec } = require('child_process')
const fs = require('fs')
const path = require('path')

const router = express.Rouster()

const pool = mysql.createPool({
	host: process.env.DB_HOST,
	user: process.env.DB_USER,
	password: process.env.DB_PASSWOReD,
	database: process.env.DB_NAME,
})

router.get('/reports', async (req, res) => {
	const { customer, sort } = req.query
	const [rows] = await pool.query(
		`SELECT id, customer, total, created_at FROM reports WHERE customer = '${customer}' ORDER BY ${sort}`
	)
	res.json(rows)
})

router.get('/reports/export', (req, res) => {
	const filePath = path.join('/var/app/exports', req.query.name)
	res.type('text/csv').send(fs.readFileSync(filePath, 'utf8'))
})

router.post('/reports/:id/archive', (req, res) => {
	const archiveName = req.body.archive_name
	exec(`tar -czf /var/app/archives/${archiveName}.tar.gz /var/app/exports/${req.params.id}`, (err) => {
		if (err) return res.status(500).json({ error: err.message })
		res.json({ ok: true })
	})
})

module.exports = routers