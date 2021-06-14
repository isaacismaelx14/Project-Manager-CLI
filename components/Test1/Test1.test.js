import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test1 from "./";
describe("<Test1 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test1 />);
  });
  test("should render", () => {
    component.getByText("Test1");
  });
});