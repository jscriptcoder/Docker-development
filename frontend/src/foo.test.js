const test = require('tape')

test('Test equal', t => {
    t.equal('foo', 'foo')
    t.end()
})

test('Test ok', t => {
    t.ok(1 > 0)
    t.end()
})

test('Test true', t => {
    t.true(true)
    t.end()
})