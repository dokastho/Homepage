import React from 'react'

class MobilePage extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className='mobile'>
        <h1>Hey There 👋</h1>
        <h5>Unfortunately, this site won't work on mobile.</h5>
      </div>
    );
  }
}

export default MobilePage;
